def evaluaEdad(edad):
    if edad<0:
        #raise TypeError("La edad no puede ser negativa")
        raise ZeroDivisionError("La edad no puede ser negativa")

    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate..."
    else:
        return "Ingrese una edad correcta"

print(evaluaEdad(-10))