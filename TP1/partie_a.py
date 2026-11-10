# TP1 - Partie A
# Exercice 1 : Dictionnaire d'étudiants

etudiants = {
    "Alice": 12.0,
    "Bob": 15.0,
    "Claire": 9.5
}




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

    # On cherche le nom associé à la meilleure note.
    nom = max(d, key=d.get)
    return (nom, d[nom])



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
                    # Chaque ligne contient un nom et une note séparés par deux-points.
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


if __name__ == "__main__":
    from pathlib import Path

    # Le fichier reste dans le dossier du script, quel que soit le dossier de lancement.
    fichier = Path(__file__).with_name("etudiants.txt")
    print("Moyenne :", moyenne_classe(etudiants))
    print("Meilleur étudiant :", meilleur_etudiant(etudiants))
    sauvegarder(etudiants, fichier)
    print("Notes rechargées :", charger(fichier))
