def numeroPar(num):
    if num % 2 == 0:
        return True


lista_de_numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numeroPar, lista_de_numeros)))
print(list(filter(lambda numero_par: numero_par%2==0, lista_de_numeros)))