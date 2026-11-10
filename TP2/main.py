from grille import Grille
from joueurs import JoueurHumain, JoueurIA


def jouer(joueur_x, joueur_o, afficher=True):
    grille = Grille()
    joueurs = {"X": joueur_x, "O": joueur_o}
    symbole = "X"
    while True:
        if afficher:
            grille.afficher()
            print("Au tour de", symbole)
        x, y = joueurs[symbole].prochain_coup(grille.tab, symbole)
        if not grille.jouer(x, y, symbole):
            if afficher:
                print("Coup invalide, rejoue.")
            # On garde le même joueur si son coup est refusé.
            continue
        if grille.est_gagnant(symbole):
            if afficher:
                grille.afficher()
                print(symbole, "a gagné !")
            return symbole
        if grille.est_plein():
            if afficher:
                grille.afficher()
                print("Match nul")
            return "nul"
        # Le coup est terminé : on passe à l’autre joueur.
        symbole = "O" if symbole == "X" else "X"


if __name__ == "__main__":
    jouer(JoueurHumain(), JoueurIA())
