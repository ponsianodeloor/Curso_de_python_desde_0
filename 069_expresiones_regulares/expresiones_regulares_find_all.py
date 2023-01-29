import re

cadena = "vamos a aprender expresiones regulares con Python. Python es un lenguaje de sintaxis sencilla"

texto_a_buscar = "Python"

print(re.findall(texto_a_buscar, cadena))