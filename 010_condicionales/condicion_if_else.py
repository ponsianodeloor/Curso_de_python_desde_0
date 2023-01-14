print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad por favor: "))

if edad_usuario<18:
    print("Eres menor de edad")
elif edad_usuario>100:
    print("Edad no valida")
else:
    print("No puedes pasar")