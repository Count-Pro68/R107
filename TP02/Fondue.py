BASE = 4
fromage = 800
eau = 2
ail = 2
pain = 400

nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

nvQuantiteefromage = fromage * nbConvives / BASE
nvQuantiteeeau = eau * nbConvives / BASE
nvQuantiteeail = ail * nbConvives / BASE
nvQuantiteepain = pain * nbConvives / BASE

print("Pour faire une fondue fribourgeoise pour", nbConvives, "personnes, il vous faut :")
print(nvQuantiteefromage, "gr de fromage")
print(nvQuantiteeeau, "dl d'eau")
print(nvQuantiteeail, "gousse(s) d'ail")
print(nvQuantiteepain, "gr de pain")
