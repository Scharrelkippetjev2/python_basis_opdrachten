# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
#ik maak gebruik van lijstcomprehensie [0] om de namen van de lijst met tuples te pakken. 
#Zou ik [1] gebruiken dan komt de prijs eruit.

beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

    # Hier de rest van jouw code...
if keuze in [topping[0] for topping in toppings]:
    prijs = [topping[0] for topping in toppings].index(keuze)
    prijs = toppings[prijs][1]
    print(f"U heeft {keuze} besteld. Dat kost {prijs:.2f}")
else:
    print(f"Uw keuze {keuze} zit niet in ons assortiment.")