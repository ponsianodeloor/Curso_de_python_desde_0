import re

cadena = "vamos a aprender expresiones regulares"

texto_a_buscar = "aprender"

texto_encontrado = re.search(texto_a_buscar, cadena)

print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())