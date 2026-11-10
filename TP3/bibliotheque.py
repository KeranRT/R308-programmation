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
