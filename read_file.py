#Leer un archivo linea por linea
"""with open("caperucita.txt", "r") as file:
    for lineas in file:
        print(lineas.strip())"""

#leer todas las lineas en una lista
"""with open("caperucita.txt", "r") as file:
    lines = file.readlines()
    print(lines)"""

#Añadir texto
"""with open('caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""
#Sobreescribir el texto
with open('caperucita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")


