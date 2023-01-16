def generaPares(limite):
    num = 1
    miLista = []

    while num<limite:
        miLista.append(num*2)
        num = num + 1

    return miLista

print(generaPares(10))

def generadorParesYield(limite):
    num = 1
    while num<limite:
        yield num * 2
        num = num+1

devuelve_pares = generadorParesYield(10)

for i in devuelve_pares:
    print(i)

print("------")
devuelve_pares_2 = generadorParesYield(10)
print(next(devuelve_pares_2))
print(next(devuelve_pares_2))