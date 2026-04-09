import re


def validate_password(password: str) -> dict:
    """
    Valide un mot de passe selon des critères de sécurité.

    Critères :
    - Longueur minimale de 8 caractères (espaces non comptés)
    - Au moins une lettre majuscule
    - Au moins une lettre minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial (!@#$%^&*...)

    Retourne un dict avec 'valid' (bool) et 'errors' (list).
    """
    if not isinstance(password, str):
        return {"valid": False, "errors": ["Le mot de passe doit être une chaîne de caractères."]}

    errors = []

    if len(password.strip()) < 8:
        errors.append("Le mot de passe doit contenir au moins 8 caractères.")

    if not re.search(r"[A-Z]", password):
        errors.append("Le mot de passe doit contenir au moins une majuscule.")

    if not re.search(r"[a-z]", password):
        errors.append("Le mot de passe doit contenir au moins une minuscule.")

    if not re.search(r"\d", password):
        errors.append("Le mot de passe doit contenir au moins un chiffre.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Le mot de passe doit contenir au moins un caractère spécial.")

    return {"valid": len(errors) == 0, "errors": errors}


if __name__ == "__main__":
    tests = ["abc", "password", "Password1", "Password1!", "        ", None]
    for pwd in tests:
        result = validate_password(pwd)
        status = "OK" if result["valid"] else "INVALIDE"
        print(f"[{status}] '{pwd}'")
        for err in result["errors"]:
            print(f"  - {err}")
