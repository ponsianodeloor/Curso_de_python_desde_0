#la impresion a la hora de imprimir en una sola linea
for i in ["App", "Tics", 1989]:
    print("hola", i, end="")

#validar correo electronico
email = False
for i in "ponsianodeloor@gmail.com":
    if i == "@":
        email = True

if email == True:
    print("Email correcto")
else:
    print("Email no es correcto")
