# Opdracht 2 lists
# Naam student: Jesse Jansen
# Groep: IT1X


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())

print("deel 1")
# print de naam van de 1e rivier:
print(rivieren[0].capitalize())
#print het 2e land waar de 1e rivier doorheen stroomt met hoofdletter:
print(rivier_info['rijn'][1].capitalize())

print("\ndeel 2")
#print naam 2e rivier
print(rivieren[1].capitalize())
#print het eerste land waar de eerste rivier doorheen stroomt.
print(rivier_info['rijn'][0].capitalize())

print("\ndeel 3")
#print naam 3e rivier
print(rivieren[2].capitalize())
#print het derde land waar de eerste rivier doorheen stroomt.
print(rivier_info['rijn'][2].capitalize())