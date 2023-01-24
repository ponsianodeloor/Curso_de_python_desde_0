edad = input("introduce la edad")
while edad.isdigit() == False:
    print("Por favor introduce un valor numerico")
    edad = input("introduce la edad")

if int(edad) > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")