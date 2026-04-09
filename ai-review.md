# AI Review — Validateur de mot de passe

## Ce que l'IA a généré

Le fichier `password_validator.py` a été entièrement généré par Claude (IA).
Il contient une fonction `validate_password(password)` qui :

- Vérifie la longueur minimale (8 caractères)
- Contrôle la présence d'une majuscule, d'une minuscule, d'un chiffre et d'un caractère spécial
- Retourne un dictionnaire `{ "valid": bool, "errors": list }` pour une intégration facile
- Inclut un bloc `__main__` avec des cas de test pour validation rapide

## Ce qui a été modifié / vérifié manuellement

- **Tests exécutés** : la sortie a été vérifiée manuellement (`python3 password_validator.py`) avant tout commit
- **Regex revue** : le pattern des caractères spéciaux a été contrôlé pour éviter des faux négatifs
- **Messages d'erreur** : reformulés en français clair pour l'utilisateur final
- **Structure du retour** : choix du `dict` plutôt qu'une simple liste confirmé pour faciliter l'usage en API

## Pourquoi Git est essentiel quand on travaille avec l'IA

### 1. Traçabilité de l'origine du code
Le `Co-Authored-By` dans le commit identifie explicitement que le code vient d'une IA.
Sans Git, impossible de savoir après coup qui a écrit quoi.

### 2. Isolation des changements
Travailler sur une branche dédiée (`feat/ai-password-validator`) permet de tester
le code généré sans polluer `main`. Si le code est mauvais, on supprime la branche.

### 3. Revue avant merge
La Pull Request oblige à relire le code de l'IA avant de l'intégrer.
L'IA peut générer du code fonctionnel mais non conforme aux standards du projet.

### 4. Rollback facile
Si un bug est introduit par du code IA en production, `git revert` ou `git bisect`
permettent d'identifier et d'annuler le changement précisément.

### 5. Diff clair = revue humaine obligatoire
Le `git diff` force à lire chaque ligne générée. On ne merge pas en aveugle.
L'IA accélère l'écriture, Git garantit la qualité et la responsabilité.

---

> **Conclusion** : l'IA génère vite, Git garantit la maîtrise.
> Le binôme IA + Git = vitesse sans perte de contrôle.
