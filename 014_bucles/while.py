i = 1
while i < 10:
    print(" Ejecucion")
    i += 1

# validar la edad de una persona
edad = int(input("Ingrese la edad de una persona"))

while edad == 0:
    print("Has introducido una edad negativa. vuelve a intentarlo")
    input("Ingresa la edad de una persona: ")
    edad -= 1
    print(f"La edad se va reduciendo {edad}")

print("gracias por colaborar, puedes pasar")
print("Edad " + str(edad))
