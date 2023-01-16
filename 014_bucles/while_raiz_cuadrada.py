import math

print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hayar la raiz de un numero negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break
    numero = input(input("Introduce un numero por favor: "))

    if numero < 0:
        intentos += 1
if intentos<2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))