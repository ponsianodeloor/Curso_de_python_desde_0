def areaCuadrado(lado):
    """Calcula el area de un cuadrado elevando al cuadrado
    :param lado:
    :return:
    """
    return f"El area del cuadrado es {lado*lado}"

def areaTriangulo(base, altura):
    return f"El area del cuadrado es {(base*altura)/2}"

print(areaCuadrado(10))
print(areaTriangulo(10,5))

print(areaCuadrado.__doc__)

help(areaCuadrado)