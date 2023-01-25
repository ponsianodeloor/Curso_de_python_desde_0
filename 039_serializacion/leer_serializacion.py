import pickle

archivo = open("lista_nombres", "rb")

lista = pickle.load(archivo)

print(lista)
