# Schrijf een Python-programma dat aan de gebruiker twee vragen stelt:
# 1. Hoeveel mensen gaan er naar het concert?
# 2. Wat is de prijs per ticket?
#
# Bereken het totaalbedrag en print dat bedrag.
#
# Voorbeeldinvoer:
# Hoeveel mensen gaan er naar het concert?  3
# Wat is de prijs per ticket?  10.55
#
# Voorbeelduitvoer:
# De totale prijs bedraagt 31.65 euro.


mensen = int(input("Hoeveel mensen gaan naar het concert? "))

prijs = int(input("Wat is de prijs per ticket? "))

totale_prijs = prijs * mensen

print("In totaal kost het", totale_prijs)
