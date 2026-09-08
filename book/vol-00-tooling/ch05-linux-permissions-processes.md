# Volume 00 — Tooling
# Chapter 5: Linux II — Permissions, Users, sudo, and Processes

> **Why this chapter:** every "Permission denied", every Dockerfile `USER` line, every
> Kubernetes securityContext, every "the training job is hogging the GPU — kill it" moment
> runs on what's here. Chapter 4 taught you *where* things are; this one teaches *who may
> touch them* and *what is running*.

---

## Warm-up — story problems (paper, 10 min, before reading)

1. **The shared flat.** Three flatmates share one flat: a common kitchen, and each person has
   their own locked bedroom. The landlord holds a master key that opens every door. Map these onto: your home directory, `/etc`, another user's
   home, and "root". Who is the landlord? What is the master key?
2. **The lending library.** A library book can be *read* by anyone, *written in* by nobody
   (except the librarian who stamps it), and *carried out* only by members. Three separate
   permissions on one object — name them in your own words. Now: a *program file* — what would
   "carrying it out" mean?
3. **The restaurant kitchen.** Ten cooks (processes) share one stove (CPU) and one fridge
   (memory). One cook has been frying the same egg for an hour, blocking a burner. The head
   chef needs to (a) *see* who's on which burner, and (b) *tell* that cook to stop — politely
   first, then not politely. Name the two levels of "stop" in your own words.

Each is a section below in disguise.

---

## 1. Decoding `ls -l` — the wall of letters

You've seen this since Day 2:

```
-rw-r--r--  1 azureuser azureuser  464 Sep  3 09:15 id_ed25519_private_gh.pub
drwx------  2 azureuser azureuser 4096 Sep  3 06:09 .ssh
lrwxrwxrwx  1 azureuser azureuser   62 Jul  2 08:41 cloudfiles -> /mnt/batch/...
```

The first column is **ten characters**, and each has a fixed meaning:

```
 d  rwx  r-x  r--
 │   │    │    │
 │   │    │    └── others  (everyone else on the machine)
 │   │    └─────── group   (users in the file's group)
 │   └──────────── owner   (the user who owns the file)
 └──────────────── type:  -  regular file
                          d  directory
                          l  symbolic link (a pointer to another path)
```

Three **classes** (owner / group / others), each with three **bits**:

| Bit | On a file | On a directory |
|---|---|---|
| `r` read | view contents | list what's inside (`ls`) |
| `w` write | modify contents | create/delete/rename entries *inside* it |
| `x` execute | run it as a program | **enter** it (`cd`) and reach things inside |

`-` means the bit is off. So `-rw-r--r--` reads: *regular file; owner may read+write; group
may read; others may read.* And `drwx------` reads: *directory; owner may do everything;
nobody else may even look inside.* That's `.ssh` — and it **must** be that way: SSH refuses
to use keys in a directory anyone else can read. You saw this rule bite on Day 2
(the private key at `-rw-------` = 600).

The `x` on directories is the one that surprises everyone: a directory with `r` but no `x`
lets you *list names* but not *open* anything inside. `x` without `r`: you can reach a file
if you already know its exact name, but can't list the directory. Both are real setups.

After the permissions: `1` = link count (ignore for now), then **owner**, then **group**,
then size in bytes, then modification time, then name.

## 2. Permissions as numbers — octal

Each class's three bits are a 3-bit number: r=4, w=2, x=1. Add them.

| Letters | Sum | Digit |
|---|---|---|
| `rwx` | 4+2+1 | 7 |
| `rw-` | 4+2 | 6 |
| `r-x` | 4+1 | 5 |
| `r--` | 4 | 4 |
| `---` | 0 | 0 |

Three classes → three digits. `rw-r--r--` = **644**. `rwx------` = **700**.
`rwxr-xr-x` = **755**. `rw-------` = **600**.

Why octal? Because three bits is exactly one base-8 digit — the notation isn't a convention,
it's forced by the bit count (same flavor of argument as `x**0.5` being forced to mean √x).

The four you'll type for the rest of your life:
- **644** — normal file: I edit, everyone reads (configs, source code)
- **600** — private file: only me (SSH keys, tokens, `.env`)
- **755** — program or directory: I edit, everyone may run/enter
- **700** — private directory (`.ssh`)

## 3. Changing ownership and permissions

| Command | Does |
|---|---|
| `chmod 600 file` | set permissions by number |
| `chmod u+x script.sh` | symbolic: **u**ser +**x**ecute. Classes: `u` `g` `o` `a`(all). Ops: `+` `-` `=` |
| `chmod -R 755 dir/` | recursive — **dangerous**; read §6 before using |
| `chown user:group file` | change owner (usually needs root) |
| `id` | who am I, what groups am I in |
| `groups` | just the groups |

`chmod u+x` is the one you'll use constantly: you write `run.sh`, try `./run.sh`, get
"Permission denied" — the file has no `x`. Add it. (Or run `bash run.sh`, which doesn't need
`x` because *bash* is the program being executed, and the script is just its input.)

## 4. root and sudo — the master key

**root** is user ID 0 — the account for which permissions are not checked. It can read any
file, kill any process, delete the filesystem. Nobody logs in as root on a sane machine.

Instead: **`sudo <command>`** — "**s**uperuser **do**" — run *one command* as root, then
drop back to yourself. You're allowed because `azureuser` is in the `sudo` group (check with
`groups`). The system logs every sudo call (`/var/log/auth.log` — you saw it on Day 2).

Rules of the master key:
- `sudo` only when a command *actually* fails with permission denied **and** you understand
  why root is needed. Never prophylactically.
- `sudo rm -rf` gets a full stop and a re-read of the path. The Ch 4 covenant, squared.
- If `sudo` fixes an error you don't understand, you haven't fixed it — you've hidden it.
  Classic example: `pip install` failing → `sudo pip install` → system Python corrupted.
  The right fix was a virtual environment (Phase 1).

`sudo -i` opens a root shell (prompt changes from `$` to `#`). Avoid; one-command sudo is
the habit.

## 5. Processes — what is running

A **process** is a running program: a PID (process ID), an owner, a parent, a state, and
a share of CPU and memory. Everything on the machine — your shell, `ls`, Python, the GPU
driver daemon — is a process. Your shell spawns a child process for every command you type.

| Command | Job |
|---|---|
| `ps aux` | snapshot of all processes (user, PID, %CPU, %MEM, command). Pipe to `grep` |
| `ps aux \| grep python` | find your Python processes |
| `top` | live view, refreshing; `q` quits. Sort by memory: press `M`; by CPU: `P` |
| `htop` | prettier `top` (installed on most systems; if not, `sudo apt install htop` — note the sudo, and why) |
| `nvidia-smi` | the GPU's `top`: which process holds how much VRAM. You've run this |
| `kill <PID>` | send **SIGTERM** (15): "please shut down cleanly" |
| `kill -9 <PID>` | send **SIGKILL** (9): the kernel removes the process. No cleanup, no appeal |
| `jobs`, `&`, `fg`, `bg`, `Ctrl+Z` | background/foreground control of *your shell's* children |
| `Ctrl+C` | send SIGINT to the foreground process — the polite interrupt you use every day |

Signals are the "two levels of stop" from warm-up 3. Always `kill` (TERM) first — a
training script gets to flush its checkpoint; a database gets to close its files. `-9` is
for when TERM was ignored. Muscle memory to build: **`kill` → wait 5 seconds → `ps` again →
only then `kill -9`.**

The tie back to permissions: **you may only kill processes you own.** Killing someone
else's — or a system daemon — needs sudo. `ps aux` column 1 tells you the owner.

### Background jobs — the 30-second version

`python train.py &` — the `&` runs it in the background; the shell gives you a PID and your
prompt back. `jobs` lists your background jobs. `fg` brings one back. `Ctrl+Z` suspends the
foreground process; `bg` resumes it in the background. Full treatment (nohup, tmux —
so jobs survive your SSH disconnecting) is the next Linux chapter; you'll need it the day
you start a 6-hour training run.

## 6. The `chmod -R` covenant

`chmod -R 777 .` is the second-most-famous way to wreck a Linux box (after `rm -rf`). 777
means *anyone may do anything* — it's the permission equivalent of leaving every door open,
and it makes SSH refuse your keys, makes package managers refuse to run, and is a
security hole you can drive a bus through. **You will see it recommended on StackOverflow.
Never do it.** If a permission problem exists, identify *which* bit *which* user needs, and
set that.

---

## 7. Drills — on the VM

**A. Read**
1. `ls -la ~` — for **five** entries of your choosing, write out the ten-character string
   in words ("regular file, owner rw, group r, others r"). Include `.ssh` and one `.log`.
2. Convert those five to octal. Then verify: `stat -c '%a %n' <file>` prints the octal.
3. `ls -ld /etc /etc/shadow /tmp` — decode each. `/etc/shadow` is the password hash file:
   who can read it? `/tmp` has a `t` in the last position — `man chmod`, search for
   "sticky", one sentence on what it does. **Report.**
4. `cat /etc/shadow` — what happens? Now `sudo cat /etc/shadow | head -3` — what changed,
   and *why is this the one legitimate use of sudo in today's drills?*
5. `id` and `groups` — which group makes `sudo` work for you? **Report.**

**B. Write**
6. In `~/practice/` (rebuild it — you know how), create `secret.txt` with one line of text.
   `chmod 600` it. `ls -l` to confirm. Then `chmod 000 secret.txt` and try to `cat` it.
   You *own* the file and still can't read it — explain in one sentence why, then fix it.
7. Create `hello.sh` containing exactly two lines:
   ```
   #!/bin/bash
   echo "hello from $(whoami) on $(hostname)"
   ```
   Run `./hello.sh` — read the error. Fix it with `chmod` (symbolic form). Run again.
   Then run `bash hello.sh` on a fresh copy *without* `x` — why does this work? **Report.**
   (The first line, `#!`, is called a *shebang* — it tells the kernel which interpreter to
   hand the file to. `man execve` if curious; not required.)
8. `mkdir locked && touch locked/inside.txt && chmod 600 locked` — then try `ls locked`
   and `cat locked/inside.txt`. Decode what each error tells you about `r` vs `x` on a
   directory. Fix with the *minimum* permission change that lets you `cat` the file.

**C. Processes**
9. `ps aux | head -1` — read the column headers. Then `ps aux | grep -c .` — how many
   processes are running? Then `ps aux --sort=-%mem | head -5` — what are the top memory
   consumers on your VM? **Report.**
10. `top`, then press `M`, watch for 10 seconds, press `q`. Then `nvidia-smi` — is anything
    using the GPU right now?
11. Run `sleep 300 &` — note the PID the shell prints. `jobs`. `ps aux | grep sleep` — find
    it again; confirm the PID matches. `kill <PID>`. `jobs` again. **Report the sequence.**
12. Run `sleep 300 &` again. This time `kill -9 <PID>`. Compare the message `jobs` shows
    versus drill 11 — "Terminated" vs "Killed". One sentence on the difference.
13. Run `python3 -c "while True: pass"` in the foreground. Open a **second** SSH session
    (or a second terminal tab in VS Code). In it: `top` — find your Python at ~100% CPU.
    Note its PID. `kill <PID>` from the second terminal. Watch the first terminal.
    **Report what appeared there.**
14. Cleanup: `rm -r ~/practice`. Covenant applies.

**D. Proof of work** — paste the **Report** items (3, 4, 5, 7, 9, 11, 13) with their outputs.

## 8. Self-check (into today's log, from memory)

1. Decode `-rwxr-x---`. Octal?
2. Why must `~/.ssh` be 700 and a private key 600?
3. `r` vs `x` on a directory — what does each let you do?
4. When is `sudo` legitimate, and what's the danger of using it to "make an error go away"?
5. `kill` vs `kill -9` — what's the difference, and which do you try first? Why?
6. You own a file with permissions `000`. Can you read it? Can you `chmod` it? Why the difference?
7. What does `./hello.sh` need that `bash hello.sh` doesn't?

---
*Next: Linux III — the shell as a language: pipes, redirection (`2>&1` explained at last),
`grep`/`sed`/`awk`, environment variables and `PATH`, shell scripting basics.*
