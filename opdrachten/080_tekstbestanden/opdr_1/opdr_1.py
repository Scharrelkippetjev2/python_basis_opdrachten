# Opdracht 1 while-loops
# Naam student: JsJ
# Groep: IT1X

# Jouw code komt hier
prompt = "Wat vind je van de huidige regering? \n" \
         "Wat vind je van de Python-lessen tot nu toe?\n" \
         "Wat vind jij de mooiste stad van Nederland?\n"

active = True
lst = []
for i in range(3):
    message = input(prompt)
    lst.append(message)

fo = open('vragen.txt', "wt")
for i in lst:
    fo.write(i + "\n")
fo.close()