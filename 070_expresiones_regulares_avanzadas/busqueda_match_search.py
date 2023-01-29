import re

nombre_1 = "Ponsiano De Loor"
nombre_2 = "Thomas Sizalema"
nombre_3 = "Thomas Jefferson"

if re.match("thomas", nombre_2, re.IGNORECASE):
    print("Se ha encontrado el nombre")
else:
    print("No se ha encontrado nada")