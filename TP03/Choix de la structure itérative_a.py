n=int(input("Définissez N : "))
somme = 0                   #Je définis la valeur modifiable

for i in range(n + 1):      #en ranger
    somme = somme + i       #somme += i
    print(i)                #affiche i

print("la somme est", somme)
