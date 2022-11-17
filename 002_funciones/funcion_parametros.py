def operacionesMath(operacion, num_1, num_2):
    if(operacion == "suma"):
        resultado = num_1 + num_2
    if(operacion == "resta"):
        resultado = num_1 - num_2
    if (operacion == "multiplicacion"):
        resultado = num_1 * num_2
    if (operacion == "division"):
        resultado = num_1 / num_2

    return resultado

op = "suma"
print(operacionesMath(op, 4,5))

op = "resta"
print(operacionesMath(op, 5, 8))

op = "multiplicacion"
print(operacionesMath(op, 10, 20))

op = "division"
print(operacionesMath(op, 4, 2))
