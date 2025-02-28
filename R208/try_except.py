# 1__________

import random # Importation du module random pour générer des nombres aléatoires

# Création liste avec nombre aléatoire de 0 à 100 (de 10 à 20 nb)

tliste = random.randint(10, 20)
liste = [random.randint(0,100) for _ in range(tliste)]

# 2__________

# Boucle "folle" --> la boucle "folle" est une boucle infinie = "while True"

while True:
	index = int(input("Entrez un index de la liste : ")) # Demande d'un index à l'utilisateur
	print("valeur de l'index", index, ":", liste[index]) # Affichage de la valeur

# 3__________

# L'affichage d'erreur par ligne rouge est normal, on va utiliser "try" et "except",
#   qui va gérer une éventuelle « IndexError » de manière à ce que la boucle « folle »
#   ne se termine jamais !

# print("Liste générée est : ", liste)
while True:
    try:
        index= int(input(f"Entrez un index entre 0 et {len(liste)-1} : "))
        print("valeur à l'index", index, ":", liste[index])
    except IndexError:
        print(f"Erreur : l'index doit être compris entre 0 et {len(liste)-1}")
