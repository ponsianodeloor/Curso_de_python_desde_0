import re

lista_nombres = [
    'Ponsiano De Loor',
    'Ponwick',
    'Mireya Levy',
    'Naun James'
]

for item in lista_nombres:
    if re.findall('^Pon', item):
        print(item)
