
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
    try:        #Évite un plantage si la note est invalide
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



def sauvegarder(d, fichier):
    try:
        with open(fichier, "w", encoding="utf-8") as f:
            for nom, note in d.items():
                f.write(f"{nom}:{note}\n")
    except OSError as e:
        print("Erreur de sauvegarde :", e)




def charger(fichier):
    d = {}

    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                try:
                    nom, note = ligne.strip().split(":")
                    if not nom:
                        continue
                    d[nom] = float(note)
                except ValueError:
                    print("Ligne invalide :", ligne.strip())

    except FileNotFoundError:
        print("Fichier introuvable")
    except OSError as e:
        print("Erreur de lecture :", e)

    return d


# Exercice 3 : Tests

sauvegarder(etudiants, "tp1/etudiants.txt")

notes_chargees = charger("tp1/etudiants.txt")
print("Notes rechargées :", notes_chargees)

# Test d'un fichier inexistant
charger("tp1/inexistant.txt")