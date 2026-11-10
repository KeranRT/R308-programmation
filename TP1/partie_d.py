from partie_c import MOTS, choisir_mot, masque


def jouer(mot=None):
    if mot is None:
        mot = choisir_mot(MOTS)
    mot = mot.upper()
    if not mot or not mot.isalpha():
        print("Le mot doit contenir uniquement des lettres.")
        return False
    cache = masque(mot)
    lettres = []
    erreurs = 0
    while erreurs < 7 and "_" in cache:
        print(" ".join(cache), "Erreurs :", erreurs, "/ 7")
        print("Lettres proposées :", " ".join(lettres))
        lettre = input("Lettre : ").strip().upper()
        if len(lettre) != 1 or not lettre.isalpha():
            print("Entre une seule lettre.")
            continue
        # Une lettre déjà jouée ne compte pas comme une nouvelle erreur.
        if lettre in lettres:
            print("Lettre déjà proposée.")
            continue
        lettres.append(lettre)
        if lettre in mot:
            # On révèle toutes les positions de la lettre.
            for i in range(len(mot)):
                if mot[i] == lettre:
                    cache[i] = lettre
        else:
            erreurs += 1
    print(" ".join(cache), "Erreurs :", erreurs, "/ 7")
    if "_" not in cache:
        print("Gagné !")
        return True
    print("Perdu, le mot était", mot)
    return False


if __name__ == "__main__":
    jouer()
