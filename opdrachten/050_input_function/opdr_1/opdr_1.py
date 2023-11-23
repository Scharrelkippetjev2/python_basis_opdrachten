# Opdracht 1 input function
# Naam student:  Jesse JANSEN
# Groep: ITx1

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math

zijde_een = int(input("Geef de lengte van de eerste zijde\n"))
zijde_twee = int(input("Geef de lengte van de tweede zijde\n"))

antwoord = (math.sqrt((zijde_een * zijde_een) + (zijde_twee * zijde_twee)))

print(f'De lengte van de schuine zijde is: {antwoord}')