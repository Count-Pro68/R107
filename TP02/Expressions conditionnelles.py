for i in range(3) :
    n = int(input("Entrer un nombre entier : "))

    if n>0:
        s = ("positif")
    else :
        s = ("négatif")
    if n==0:
        s = ("égal à 0")


    if n%2==0:
        p = ("pair")
    else :
        p = ("impair")

    print("le nombre est", s, "et", p)