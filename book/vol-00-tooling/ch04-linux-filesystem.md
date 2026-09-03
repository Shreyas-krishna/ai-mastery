# Volume 00 — Tooling
# Chapter 4: Linux I — The Filesystem, Navigation, and Files

> **Why Linux, why now:** every server, every Docker container, every Kubernetes pod, every
> training job you will ever touch runs Linux. Your T4 lives in a Linux machine. From today,
> the VM is your daily workshop — Windows is just the desk it sits on.

---

## 1. One idea to rule them all: everything is a file, and files live in one tree

Windows thinks in drives: `C:\`, `D:\` — separate trees side by side. Linux has **one single
tree** rooted at `/` (called "root"). Every disk, folder, device — even your keyboard and the
GPU — appears somewhere under `/`. There is no second tree.

```
/                    ← the root: everything starts here
├── home/
│   └── <you>/       ← YOUR territory: ~ (the "home directory")
├── etc/             ← system configuration (text files!)
├── bin/, usr/       ← the programs themselves (ls, python live here)
├── var/             ← things that grow: logs, caches
├── tmp/             ← scratch space, wiped on reboot
└── dev/             ← devices as files (your GPU is /dev/nvidia0!)
```

You need only three of these for months: `~` (home — yours), `/etc` (config — read it,
don't fear it), `/var/log` (logs — where debugging lives). The rest will introduce themselves.

**An address in this tree is a path.** Two kinds, and the distinction is load-bearing:
- **Absolute path** — starts at root, begins with `/`: `/home/you/ai-mastery/code`. Works
  from anywhere, like a full postal address.
- **Relative path** — starts from *where you are now*: `code/stats`. Short, but meaning
  depends on your current location.

Two magic names exist in every folder: `.` (this folder) and `..` (the parent folder).
`../..` = grandparent. These compose: `../logs/2026-09-03.md`.

## 2. Where am I? The navigation trio

| Command | Mnemonic | What it does |
|---|---|---|
| `pwd` | print working directory | prints the absolute path of where you are |
| `ls` | list | shows what's here |
| `cd <path>` | change directory | moves you |

You know `cd`. Now its idioms: `cd` alone → jump home. `cd ..` → up one. `cd -` → jump BACK
to wherever you just were (toggle). `cd ~/ai-mastery` → home-relative path.

`ls` grows claws with flags (options after a dash):
- `ls -l` — long form: permissions, owner, size, date per line (next chapter decodes it)
- `ls -a` — all: reveals hidden files (names starting with `.` — like `.git`!)
- `ls -la` — both at once. Your workhorse.
- `ls -lh` — human sizes (4.0K not 4096)

## 3. Reading files without opening an editor

| Command | Job |
|---|---|
| `cat file` | dump whole file to screen (conCATenate) |
| `less file` | page through a big file — space=down, b=up, `/<term>`=search (e.g. `/error`), **q=quit** |
| `head -n 20 file` | first 20 lines |
| `tail -n 20 file` | last 20 lines |
| `tail -f logfile` | follow a growing file live — THE debugging command of your future |

## 4. Making and destroying things

| Command | Job | Danger |
|---|---|---|
| `mkdir name` | make directory | — |
| `mkdir -p a/b/c` | make nested path, no complaints | — |
| `touch file` | create empty file (or update its timestamp) | — |
| `cp src dst` | copy file | overwrites dst silently |
| `cp -r src dst` | copy folder (recursive) | same |
| `mv src dst` | move — also how you RENAME | overwrites silently |
| `rm file` | delete file | **NO RECYCLE BIN. GONE. FOREVER.** |
| `rm -r folder` | delete folder + contents | same, but plural |

**The `rm` covenant:** there is no undo, no trash can, no mercy. Before every `rm`, pause and
read the command once aloud (same rule as commit messages). Never run `rm -rf` on a path you
did not just `ls`. One famous class of career-ending typo: `rm -rf / home/you/stuff` — the
stray space makes it two arguments, the first being the entire filesystem root.

## 5. Helping yourself: man pages and friends

- `man ls` — the manual for any command (navigate like `less`, q to quit)
- `ls --help` — quick flag summary
- `which python` — where does this command's program actually live?
- `history` — everything you've typed; `!!` reruns the last command

`man` is the reason Linux masters seem to know everything: they don't memorize, they read.

## 6. Drills — on the VM, in order (SSH in first)

**A. Explore (no creating yet)**
1. `pwd` the moment you land. Where does SSH drop you?
2. `ls -la ~` — what hidden files already live in your home? Note two of their names.
3. Walk to `/` (absolute), `ls` it, and compare against the §1 tree. Then get home in ONE
   command, two different ways (you know two).
4. `ls /home` — who else lives on this VM?
5. Read `/etc/os-release` with `cat`. What Linux distribution and version is the VM running?
   **Report this to me.**
6. `less /var/log/syslog` (if permission denied, note that — it's foreshadowing for the
   permissions chapter). Search inside for the word "error" (you know the key from §3).
   Quit without panic.
7. `man rm` — find, in the manual itself, what the `-i` flag does. **Report it.**

**B. Build (your workshop)**
8. In `~`, create this in as few commands as possible, then prove it with `ls -R practice`:
```
practice/
├── src/
├── data/
└── notes/day1.txt        (empty file)
```
9. Rename `day1.txt` → `day01.txt` (naming law applies on Linux too). Which command renames?
10. Copy `day01.txt` into `src/`, then delete the copy — with `rm -i`, experiencing the
    safety net you just read about in the manual.
11. Put text into a file straight from the terminal:
    `echo "Day 2: the tree has one root" > notes/day01.txt` — then `cat` it to verify.
    (`>` sends a command's output into a file, replacing contents; `>>` appends. This is a
    preview of redirection — a full lesson soon.)
12. From INSIDE `practice/src`, using only relative paths: copy `../notes/day01.txt` into
    `../data/`. Verify from where you stand without cd-ing (`ls ../data`).
13. Destroy the whole `practice` tree with one command. Read it aloud first. Then prove it's
    gone.

**C. Proof of work** — paste me: your `pwd` from drill 1, the distro from drill 5, the `-i`
answer from drill 7, and the full command sequence you used for drills 8–13.

## 7. Self-check (into today's log, from memory)

1. Absolute vs relative path — define each; when does a relative path betray you?
2. What are `.` and `..`? What does `cd -` do?
3. Which command renames a file, and why does that make sense given its real job?
4. Why is `rm` more dangerous than deleting in Windows Explorer? State the covenant.
5. You need the last 50 lines of a growing log file, live. Exact command?
6. What's the difference between `>` and `>>`?
7. Where in the tree do: config files, logs, your own work — live?

---
*Next: Linux II — permissions (that `-rwxr-xr--` wall of letters), users, sudo, and processes.*
