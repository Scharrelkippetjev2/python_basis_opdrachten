# Opdracht 3 condities
# Naam student: JsJ
# Groep: IT1X




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

levensjaar = int(input("Geef u leeftijd in aantal jaar: "))

for groep in leeftijd:
#Dit stukje controleert of de leeftijd van de bezoeker binnen de leeftijdsgrenzen van de huidige cat valt.
        if leeftijd[groep][0] <= levensjaar <= leeftijd[groep][1]:
            korting = kortings_percentages[groep]

            print(f"U behoort tot de groep {groep}")
            print(f"U krijgt {korting}% korting")
            
            toegangsprijs = normale_toegangsprijs * (100 - korting) / 100
#2f staat voor 2 decimalen achter de komma.
            print(f"U betaald daarom €{toegangsprijs:.2f}")
