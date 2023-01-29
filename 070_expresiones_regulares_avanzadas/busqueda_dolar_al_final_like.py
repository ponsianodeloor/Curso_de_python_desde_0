import re

lista_nombres = [
    'Ponsiano De Loor',
    'Ponwick',
    'Mireya Levy',
    'Naun James Levy De Loor'
]

for item in lista_nombres:
    if re.findall('Loor$', item):
        print(item)
