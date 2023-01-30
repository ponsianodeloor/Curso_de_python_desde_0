def areaTriangulo(base, altura):
    """
    Calcula el area de un triangulo dado
    >>> areaTriangulo(2,4)
    5.0
    """
    return ((base * altura) / 2)

print(areaTriangulo(2, 4))

import doctest
doctest.testmod()