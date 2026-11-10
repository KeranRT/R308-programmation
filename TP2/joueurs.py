import random


class JoueurHumain:
    def prochain_coup(self, tab, symbole):
        while True:
            try:
                x = int(input("Ligne (0 à 2) : "))
                y = int(input("Colonne (0 à 2) : "))
                return x, y
            except ValueError:
                print("Entre des nombres entiers.")


class JoueurIA:
    def prochain_coup(self, tab, symbole):
        # L’IA choisit uniquement parmi les cases encore libres.
        libres = []
        for x in range(3):
            for y in range(3):
                if tab[x][y] == " ":
                    libres.append((x, y))
        if not libres:
            return None
        return random.choice(libres)
