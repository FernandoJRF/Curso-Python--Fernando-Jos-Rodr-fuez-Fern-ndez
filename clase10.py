numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Fernando",
               "Apellido": "Rodríguez",
               "altura": 1.75,
               "Edad": 22}
print(information)
del information ["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Fernando":{"Apellido": "Rodríguez",
               "altura": 1.75,
               "Edad": 22},
              "Diego": {"Apellido": "Antezana",
               "altura": 1.50,
               "Edad": 24}}
print(contacts)