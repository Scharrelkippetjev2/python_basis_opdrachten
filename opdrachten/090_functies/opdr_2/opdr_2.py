# Opdracht 1 functies
# Naam student: JsJ
# Groep: ITx1


def kilometers_naar_miles(km):
    return(f"{kilometers} miles = {kilometers / 1.609344} kilometers")

def miles_naar_kilometers(miles):
    return(f"{miles} miles = {miles * 1.609344} kilometers")

kilometers = 1223
miles = 867

print(kilometers_naar_miles(kilometers))
print(miles_naar_kilometers(miles))