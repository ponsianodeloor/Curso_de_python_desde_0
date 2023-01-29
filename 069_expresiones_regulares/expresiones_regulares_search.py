import re

cadena = "vamos a aprender expresiones regulares"

texto_a_buscar = "aprender"

if re.search(texto_a_buscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")