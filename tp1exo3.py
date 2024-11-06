jour=int(input())
heure=int(input())
minute=int(input())
minutes_ecoulees=((jour-1)*24*60)+(heure*60)+minute
print("Le nombre de minute écoulées depuis le début du mois est de {}".format(minutes_ecoulees))

