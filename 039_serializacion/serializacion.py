import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario = open("lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del fichero_binario #borrar de la memoria