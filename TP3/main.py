from pathlib import Path
from bibliotheque import Bibliotheque
from livre import Livre
from utilisateur import Utilisateur


def main():
    # La sauvegarde se trouve à côté du programme.
    fichier = Path(__file__).with_name("livres.csv")
    b = Bibliotheque()
    b.charger(fichier)
    while True:
        print("\n1 Ajouter un livre\n2 Ajouter un utilisateur\n3 Emprunter un livre")
        print("4 Rendre un livre\n5 Afficher les livres\n6 Quitter et sauvegarder")
        choix = input("Choix : ").strip()
        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            try:
                annee = int(input("Année : "))
            except ValueError:
                print("Année non numérique.")
                continue
            ok = bool(titre and auteur) and b.ajouter_livre(Livre(titre, auteur, annee))
            print("Livre ajouté." if ok else "Titre vide, auteur vide ou livre déjà présent.")
        elif choix == "2":
            ok = b.ajouter_utilisateur(Utilisateur(input("Nom : ").strip()))
            print("Utilisateur ajouté." if ok else "Nom vide ou déjà présent.")
        elif choix in ("3", "4"):
            nom = input("Nom : ").strip()
            titre = input("Titre : ").strip()
            ok = b.emprunter(nom, titre) if choix == "3" else b.rendre(nom, titre)
            print("Opération effectuée." if ok else "Opération impossible : vérifie le nom, le titre et l'emprunt.")
        elif choix == "5":
            b.afficher_livres()
        elif choix == "6":
            # En cas d’échec de sauvegarde, le menu reste ouvert.
            if b.sauvegarder(fichier):
                break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
