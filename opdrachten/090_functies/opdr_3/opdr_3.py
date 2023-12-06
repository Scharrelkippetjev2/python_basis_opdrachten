# Opdracht 1 functies
# Naam student: JsJ
# Groep:  ITX1

import math

def kubus_vol(m):
    return(f"De inhoud van deze kubus is: {zijde ** 3}")
    pass

def bol_vol(r):
    return(f"De inhoud van deze bol is: {4/3 * math.pi * (radius ** 3)}")
    pass

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))