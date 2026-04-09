# Git Cheatsheet

## Branches

```bash
git branch                        # lister les branches locales
git checkout -b <branch>          # créer et basculer sur une branche
git branch -d <branch>            # supprimer une branche locale
git push origin --delete <branch> # supprimer une branche distante
```

## Commits

```bash
git add <file>                    # stager un fichier
git commit -m "message"           # committer
git commit --amend                # modifier le dernier commit (non pushé)
git log --oneline --graph         # historique visuel
```

## Merge & Rebase

```bash
git merge <branch>                # merge standard (crée un merge commit)
git merge --squash <branch>       # fusionner en un seul commit
git rebase main                   # rejouer les commits sur main
git cherry-pick <hash>            # copier un commit sur la branche courante
```

## Remote

```bash
git remote add origin <url>       # ajouter un remote
git push -u origin <branch>       # push + tracking
git pull origin main --rebase     # pull avec rebase
git fetch --all                   # récupérer sans merger
```

## Tags

```bash
git tag -a v1.0.0 -m "message"   # tag annoté
git push origin v1.0.0            # pousser un tag
git tag -d v1.0.0                 # supprimer un tag local
```

## Annuler

```bash
git restore <file>                # annuler les modifications non stagées
git reset HEAD <file>             # déstagé un fichier
git revert <hash>                 # annuler un commit (crée un nouveau commit)
git stash                         # mettre de côté les modifications
git stash pop                     # récupérer le stash
```
