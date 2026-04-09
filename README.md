# Git Challenges

Practical Git & GitHub workflow exercises — branching, merging, rebasing, cherry-picking, tagging, and AI-assisted development.

## Contents

| File | Description |
|------|-------------|
| `password_validator.py` | Password strength validator (AI-assisted) |
| `ai-review.md` | Transparency doc: AI usage + Git rationale |
| `cherry_pick_demo.txt` | Cherry-pick workflow demo |
| `squash_demo.txt` | Squash merge demo |
| `git_cheatsheet.md` | Essential Git commands reference |

## Workflow used in this repo

```
main
 ├── feat/git-cheatsheet       → merged via PR #6
 ├── fix/password-validator    → merged via PR #7
 └── ...
```

## Key concepts practised

- `git merge --squash` — clean single commit from multiple
- `git cherry-pick` — copy a commit across branches
- `git tag -a` — annotated release tags
- Pull Requests with description and review
- AI-assisted development with full Git traceability

## Setup

```bash
git clone https://github.com/senBenz/challenges.git
cd challenges
python3 password_validator.py
```

## Release

Current version: **v1.0.0**
