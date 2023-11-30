# Opdracht 2 tekstbestanden
# Naam student: JsJ
# Groep: It1x

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....
pogingen = 0

while True:
    gebruikers_getal = int(input("raad het geheime getal: "))
    pogingen += 1
    
    if gebruikers_getal == geheim_getal:
        print("je hebt het getal geraden!")
        break
    elif gebruikers_getal > geheim_getal:
        print("lager")
    else:
        print("hoger")
print(f"het getal was {geheim_getal}")
print(f"je hebt het in {pogingen} keer gedaan!")