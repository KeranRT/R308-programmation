import random


def jouer():
    # Les deux bornes sont incluses dans le tirage.
    secret = random.randint(1, 100)
    essais = 0
    while essais < 10:
        try:
            nombre = int(input("Nombre entre 1 et 100 : "))
        except ValueError:
            print("Entre un nombre entier.")
            continue
        if not 1 <= nombre <= 100:
            print("Le nombre doit être entre 1 et 100.")
            continue
        # Seules les propositions valides comptent comme un essai.
        essais += 1
        if nombre == secret:
            print("Gagné !")
            return True
        print("Trop petit" if nombre < secret else "Trop grand")
    print("Perdu, le nombre était", secret)
    return False


if __name__ == "__main__":
    jouer()
