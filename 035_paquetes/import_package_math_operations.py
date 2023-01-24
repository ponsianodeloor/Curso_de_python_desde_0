from calculos.OperacionesMatematicas import *
from calculos.fn_operaciones_matematicas import *
#import calculos.fn.operaciones_matematicas

op_math = OperacionesMatematicas(10.5, 2)

print("La suma es: ", op_math.suma())
print("La resta es: ", op_math.resta())
print("La multiplicación es: ", op_math.multiplicacion())
print("La división es: ",op_math.division())
print("La potencia es: ", op_math.potencia())
print("El redondeo es: ",op_math.redondear())

#fn_op_math = calculos.fn.operaciones_matematicas
print(suma(1,2))
print(resta(1,2))
print(multiplicacion(1,2))
print(division(1,2))
print(potencia(1,2))
print(redondear(5.30))