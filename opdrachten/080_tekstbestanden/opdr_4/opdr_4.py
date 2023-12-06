# Opdracht 4 Tekst opslaan
# Naam student: JsJ
# Groep: itx1


# Party enquete

prompt_1 = "Wat is je voornaam?"
prompt_2 = "Wat is je achternaam?"
prompt_3 = "Wat neem je mee aan drank?"
prompt_4 = "Wat neem je mee om te eten?"

active = True
lst = []
while active:
    message = input(prompt_1)
    if message == input():
        active = False
        fo = open('feestgangers.txt', 'wt')
        for i in lst:
            fo.write("Wat is je voornaam?" + "\n" + i + "\n")
        fo.close()
    else:
        lst.append(message)


active = True
lst = []
while active:
    message = input(prompt_2)
    if message == input():
        active = False
        fo = open('feestgangers.txt', 'a+')
        for i in lst:
            fo.write("Wat is je achternaam?" + "\n" + i + "\n")
        fo.close()
    else:
        lst.append(message)

active = True
lst = []
while active:
    message = input(prompt_3)
    if message == input():
        active = False
        fo = open('feestgangers.txt', 'a+')
        for i in lst:
            fo.write("Wat neem je mee aan drank?" + "\n" + i + "\n")
        fo.close()
    else:
        lst.append(message)

active = True
lst = []
while active:
    message = input(prompt_4)
    if message == input():
        active = False
        fo = open('feestgangers.txt', 'a+')
        for i in lst:
            fo.write("Wat neem je mee om te eten?" + "\n" + i + "\n")
        fo.close()
    else:
        lst.append(message)
print("bedaknt voor het instivuuleen! \nSee tou at the party.")