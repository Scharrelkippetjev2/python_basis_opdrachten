# Opdracht 3 Tekst opslaan
# Naam student: JsJ
# Groep: ITx1


# input waar je letters uit haalt.
# de letter moet omgezet worden in unicode ( ord('') ) zodat er mee gerekent kan worden
# dan moet de letter allemaal stuk voor stuk omgezt worden met chr('')

tekst = input("geef de tekst die je wilt encrypten")
for x in tekst:
    unicode = ord(x)
    encrypt = unicode + 5
    decrypt = chr(encrypt)
    print(decrypt)

#decrypt unicode
