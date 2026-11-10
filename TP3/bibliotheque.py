import csv

from livre import Livre
from utilisateur import Utilisateur


class Bibliotheque:
    def __init__(self):
        # Les titres et les noms servent de clés pour retrouver les objets.
        self.livres = {}
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        if not livre.titre.strip() or livre.titre in self.livres:
            return False
        self.livres[livre.titre] = livre
        return True

    def ajouter_utilisateur(self, utilisateur):
        if not utilisateur.nom.strip() or utilisateur.nom in self.utilisateurs:
            return False
        self.utilisateurs[utilisateur.nom] = utilisateur
        return True

    def emprunter(self, nom, titre):
        if nom not in self.utilisateurs or titre not in self.livres:
            return False
        return self.utilisateurs[nom].emprunter_livre(self.livres[titre])

    def rendre(self, nom, titre):
        if nom not in self.utilisateurs or titre not in self.livres:
            return False
        return self.utilisateurs[nom].rendre_livre(self.livres[titre])

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre.")
        for livre in self.livres.values():
            livre.afficher()


    def sauvegarder(self, fichier):
        try:
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                # La première ligne indique le nom de chaque colonne du CSV.
                writer.writerow(["titre", "auteur", "année", "disponible", "emprunteur"])
                for l in self.livres.values():
                    writer.writerow([l.titre, l.auteur, l.annee, l.disponible, l.emprunteur or ""])
            return True
        except OSError as e:
            print("Erreur de sauvegarde :", e)
            return False

    def charger(self, fichier):
        try:
            with open(fichier, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                champs = {"titre", "auteur", "année", "disponible", "emprunteur"}
                if not champs.issubset(reader.fieldnames or []):
                    print("En-tête CSV invalide.")
                    return False
                # On prépare les données avant de remplacer la bibliothèque actuelle.
                nouvelle = Bibliotheque()
                for ligne in reader:
                    try:
                        titre = ligne["titre"]
                        auteur = ligne["auteur"]
                        annee = int(ligne["année"])
                        dispo = ligne["disponible"]
                        nom = ligne["emprunteur"]
                        if not titre or not auteur or dispo not in ("True", "False"):
                            raise ValueError
                        if dispo == "False" and not nom:
                            raise ValueError
                        if dispo == "True" and nom:
                            raise ValueError
                        if not nouvelle.ajouter_livre(Livre(titre, auteur, annee)):
                            raise ValueError
                        # On recrée aussi l’utilisateur et sa liste d’emprunts.
                        if dispo == "False":
                            if nom not in nouvelle.utilisateurs:
                                nouvelle.ajouter_utilisateur(Utilisateur(nom))
                            nouvelle.emprunter(nom, titre)
                    except (ValueError, TypeError, KeyError):
                        print("Ligne CSV invalide, ignorée.")
                self.livres = nouvelle.livres
                self.utilisateurs = nouvelle.utilisateurs
            return True
        except FileNotFoundError:
            return False
        except (OSError, UnicodeError, csv.Error) as e:
            print("Erreur de lecture :", e)
            return False
