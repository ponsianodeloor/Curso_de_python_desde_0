tupla = ("Ponsiano", 19, 10, 1989, 19)
print(tupla[2])

lista = list(tupla)

print(lista[:])

nueva_tupla = tuple(lista)
print(nueva_tupla)

print("Ponsiano" in nueva_tupla)

print(nueva_tupla.count(19))

print(len(nueva_tupla))

tupla_unitaria = ("Ponsiano",)
print(len(tupla_unitaria))