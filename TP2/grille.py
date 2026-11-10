class Grille:
    def __init__(self):
        # Chaque ligne possède sa propre liste de trois cases.
        self.tab = [[" " for _ in range(3)] for _ in range(3)]

    def afficher(self):
        for i, ligne in enumerate(self.tab):
            print(" | ".join(ligne))
            if i < 2:
                print("---------")

    def jouer(self, x, y, joueur):
        if joueur not in ("X", "O"):
            return False
        # On vérifie les coordonnées avant de lire la case.
        if not (0 <= x < 3 and 0 <= y < 3):
            return False
        if self.tab[x][y] != " ":
            return False
        self.tab[x][y] = joueur
        return True

    def est_gagnant(self, j):
        if j not in ("X", "O"):
            return False
        # On vérifie les trois lignes et les trois colonnes.
        for i in range(3):
            if all(self.tab[i][k] == j for k in range(3)):
                return True
            if all(self.tab[k][i] == j for k in range(3)):
                return True
        # Il reste les deux diagonales à vérifier.
        return (all(self.tab[i][i] == j for i in range(3))
                or all(self.tab[i][2-i] == j for i in range(3)))

    def est_plein(self):
        return all(case != " " for ligne in self.tab for case in ligne)
