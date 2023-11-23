# Opdracht 1 lists
# Naam student: Jesse Jansen
# Groep: IT1X


#maakt lijst aan:
mylist = []

#maak direc aan:
dict_1 = { "id": 1, "voornaam": "Coen", "achternaam": "Hubert" }
#omdat python bij 0 begint met tellen en je de 2e naam wil weten schrijf je bij print 1 neer.
dict_2 = { "id": 2, "voornaam": "Jolijn", "achternaam": "Evert" }
dict_3 = { "id": 3, "voornaam": "Melle", "achternaam": "Lia" }
dict_4 = { "id": 4, "voornaam": "Otte", "achternaam": "Jozef" }

#directie toevoiegen aan de lijst:
mylist.append(dict_1)
mylist.append(dict_2)
mylist.append(dict_3)
mylist.append(dict_4)

#laat lijst zien met de 2e persoon op het scherm
print(mylist[1]["voornaam"], mylist[1]["achternaam"])