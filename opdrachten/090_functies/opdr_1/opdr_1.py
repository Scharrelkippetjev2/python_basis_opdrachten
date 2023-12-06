# Opdracht 1 functies
# Naam student: Jsj
# Groep: ITx1


def write_to_file(afile, atext):
    prompt_1 = "Zet hier wat tekst"
    active = True
    lst = []
    while active:
        message = input(prompt_1)
        if message == input():
            active = False
            fo = open('text.txt', 'at')
            for i in lst:
                fo.write(i + "\n")
            fo.close()
        else:
            lst.append(message)
    pass

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
