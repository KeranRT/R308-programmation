class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        return False

    def rendre_livre(self, livre):
        # Seul l’utilisateur qui a emprunté le livre peut le rendre.
        if livre not in self.emprunts or livre.emprunteur != self.nom:
            return False
        if livre.rendre():
            self.emprunts.remove(livre)
            return True
        return False

    def afficher_emprunts(self):
        if not self.emprunts:
            print("Aucun emprunt.")
        for livre in self.emprunts:
            livre.afficher()
