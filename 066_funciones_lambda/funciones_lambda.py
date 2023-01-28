def areaTriangulo(base, altura):
    return (base * altura) / 2

triangulo_1 = areaTriangulo(5, 7)
triangulo_2 = areaTriangulo(9, 6)

print(triangulo_1)
print(triangulo_2)

areaTrianguloLambda = lambda base, altura:(base*altura)/2
triangulo_1 = areaTrianguloLambda(5, 7)
triangulo_2 = areaTrianguloLambda(9, 6)

print(triangulo_1)
print(triangulo_2)