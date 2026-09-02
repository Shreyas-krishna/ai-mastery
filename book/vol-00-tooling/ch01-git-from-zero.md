# Volume 00 — Tooling
# Chapter 1: Git From Absolute Zero

> **Why this is lesson #1:** Every single artifact you produce for the next 16 months — code,
> notes, exams, projects — lives in git. Every MANGA company runs on it. Your GitHub contribution
> graph is part of your public brand. And you'll practice it every day until it's a reflex.

---

## 1. The problem git solves

Imagine you're writing code. You get something working. You change it to try an idea. The idea
fails, and now you can't remember what the working version looked like. So you start making copies:
`model.py`, `model_v2.py`, `model_final.py`, `model_final_ACTUALLY.py`. Sound familiar? That mess
is what 5 years of notebooks looks like — and git is its cure.

**Git is a time machine for a folder.** It lets you:
1. Save a *snapshot* of your entire folder at any moment (a **commit**)
2. See the full history of every snapshot ever taken
3. Jump back to any snapshot
4. Work on ideas in parallel universes (**branches**) and merge them
5. Synchronize all of this with a copy on another machine (**remote** — e.g., GitHub, your VM)

## 2. The three zones — the mental model everything rests on

A folder managed by git (a **repository** or "repo") has three zones:

```
  WORKING DIRECTORY  --->   STAGING AREA   --->    REPOSITORY
  (your real files)        (the loading dock)     (permanent history)
        edit                  git add                git commit
```

1. **Working directory** — the actual files you see and edit. Nothing special.
2. **Staging area** (the "index") — a loading dock. You *choose* which changes go into the next
   snapshot by placing them here with `git add`. This is deliberate: a commit should be one
   logical change, not "everything I touched today."
3. **Repository** (the `.git` folder) — the permanent, append-only history of snapshots.
   `git commit` takes whatever is on the loading dock and seals it into history forever, with a
   message, a timestamp, an author, and a unique ID (a *hash* — you'll learn what hashes really
   are in the DSA volume; for now: a fingerprint of the snapshot's content).

**Everything in git is a movement between these three zones.** When confused, ask: "which zone
is my change in right now?" `git status` answers exactly that question — it will be the command
you run most in your life.

## 3. First contact — your commands for today

Only these today. Branching, merging, remotes come in Chapters 2–3.

| Command | What it does (in zone language) |
|---|---|
| `git init` | Turns the current folder into a repo (creates the hidden `.git` folder) |
| `git status` | Shows what's changed in the working dir, what's staged, what's untracked |
| `git add <file>` | Moves a file's current state onto the loading dock |
| `git add .` | Stages everything changed (use consciously, not by habit) |
| `git commit -m "message"` | Seals the loading dock's contents into history |
| `git log` | Shows the history of commits (newest first). `git log --oneline` for compact view |
| `git diff` | Shows unstaged changes (working dir vs staging) |
| `git diff --staged` | Shows staged changes (staging vs last commit) |
| `git restore <file>` | DANGER: throws away unstaged edits, restores file from last snapshot |

**Commit message rule from day 1:** imperative mood, says *what and why*, under ~70 chars.
Good: `Add chapter 1 git lesson`. Bad: `stuff`, `changes`, `asdf`. I will call these out.

## 4. One-time setup

Git stamps every commit with your identity. Config exists at two levels: `--global` (your whole
machine) and **local** (this repo only — overrides global). Because this is a work machine but a
*personal* program, we keep identities separated:

```
git config --global init.defaultBranch main
```

Then, INSIDE the ai-mastery folder (after `git init` in drill 1), set your PRIVATE identity
locally — this repo belongs to your private GitHub account, never the org one:

```
git config user.name  "Your Name"
git config user.email "your-private-email@example.com"
```

Verify with `git config user.email` (run inside the repo). **Rule:** every personal repo gets
local identity set immediately after `git init`. Org email in a personal repo = commits don't
count on your GitHub profile + employer identity stamped on personal work.

## 5. Drills — do these now, in order, in a terminal

Open a terminal in `C:\Users\shreyas.krishna\ai-mastery` and:

1. Run `git init`. Then run `git status`. **Read every line of the output.** What does
   "untracked files" mean, in zone language?
2. Run `git add ROADMAP.md`, then `git status` again. What changed in the output? Which zone
   is ROADMAP.md's content in now?
3. Commit it: `git commit -m "Add program roadmap"`. Run `git status` and `git log`.
4. Stage and commit the rest: the `book/` and `logs/` folders (one commit each, with proper
   messages — think about what each commit *is*).
5. Open `ROADMAP.md`, change anything trivial (add a space somewhere). Run `git diff` and find
   your change in the output (`-` lines = old, `+` lines = new). Then run `git restore ROADMAP.md`
   and confirm with `git diff` that the change is gone. You just used the time machine.
6. Create a throwaway file `scratch.txt` with any text. Stage it. Then *change it again* without
   re-adding. Run `git status` — the file appears **twice** (staged AND modified). Explain to
   yourself why, in zone language. This trips up people with 10 years of experience.
   Then delete it: `del scratch.txt`, then `git add scratch.txt`, commit. Yes — deletions are
   staged too. A snapshot records absence as much as presence.

## 6. Self-check (answer without looking up — write answers at the bottom of today's log)

1. What are the three zones and what command moves content between each pair?
2. Why does the staging area exist at all? Why not commit the working directory directly?
3. What is a commit, precisely? What five things does it contain (per §2)?
4. In drill 6, why did `scratch.txt` show up as both staged and modified?
5. `git diff` shows nothing but `git diff --staged` shows changes. What state am I in?

**Gate for this chapter** comes at the end of Phase 0 as part of Gate 0, but I will quiz you on
these in your debrief today.

---
*Next chapter: 2 — Branches, merges, and how git thinks (the commit graph). Then 3 — Remotes, GitHub, SSH.*
