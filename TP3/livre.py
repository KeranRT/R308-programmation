class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        # Aucun utilisateur n’a encore emprunté ce livre.
        self.emprunteur = None

    def afficher(self):
        etat = "disponible" if self.disponible else "emprunté par " + self.emprunteur
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")

    def emprunter(self, nom):
        # Un livre ne peut avoir qu’un seul emprunteur à la fois.
        if not self.disponible or not nom:
            return False
        self.disponible = False
        self.emprunteur = nom
        return True

    def rendre(self):
        if self.disponible:
            return False
        self.disponible = True
        self.emprunteur = None
        return True
