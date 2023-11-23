# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

stadlijst = []
maxlengte = 5
while len(stadlijst) < maxlengte:
    stad = input("wilt u de volgende stad invoeren: Amsterdam, Zwolle, Dronten, Haarlem, Zaanstad? ")
    stadlijst.append(stad)
    print(f'{stadlijst}')

stadlijst.sort(reverse=True, key=lambda stad: stad.lower())
print('\nGesoorteerd lijstje reverse:')
print(f'{stadlijst}')