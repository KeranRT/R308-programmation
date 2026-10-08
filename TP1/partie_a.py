
# TP1 - Partie A
# Exercice 1 : Dictionnaire d'étudiants

etudiants = {
    "Alice": 12.0,
    "Bob": 15.0,
    "Claire": 9.5
}

print(etudiants)


# Exercice 2 : Fonctions

def ajouter_etudiant(d, nom, note):
    try:
        d[nom] = float(note)
    except (ValueError, TypeError):
        print("Erreur : note invalide")


def moyenne_classe(d):
    if len(d) == 0:
        return 0
    return round(sum(d.values()) / len(d), 2)


def meilleur_etudiant(d):
    if len(d) == 0:
        return None

    nom = max(d, key=d.get)
    return (nom, d[nom])



# Test des fonctions

ajouter_etudiant(etudiants, "David", 17)
ajouter_etudiant(etudiants, "Alice", 14)

print("Étudiants :", etudiants)
print("Moyenne :", moyenne_classe(etudiants))
print("Meilleur étudiant :", meilleur_etudiant(etudiants))


