import random

MOTS = ["python", "reseau", "routeur", "ordinateur", "ÉLÉPHANT"]


def choisir_mot(liste):
    if not liste:
        return ""
    # On utilise les majuscules pour comparer les lettres plus facilement.
    return random.choice(liste).upper()


def masque(mot):
    # Une case du masque correspond à une lettre du mot.
    return ["_"] * len(mot)


if __name__ == "__main__":
    mot = choisir_mot(MOTS)
    print(masque(mot))
