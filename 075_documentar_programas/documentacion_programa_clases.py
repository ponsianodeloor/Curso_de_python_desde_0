class Area():
    """
    Esta clase calcula las areas de diferentes figuras geometricas
    """
    def areaCuadrado(lado):
        """Calcula el area de un cuadrado elevando al cuadrado
        :param lado:
        :return:
        """
        return f"El area del cuadrado es {lado*lado}"

    def areaTriangulo(base, altura):
        """
        se calcula un triangulo sin pitagoras
        :param altura:
        :return:
        """
        return f"El area del cuadrado es {(base*altura)/2}"

print(Area.areaCuadrado(10))
print(Area.areaTriangulo(10,5))

print(Area.areaCuadrado.__doc__)

help(Area)