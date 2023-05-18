elementos = ['Ponsiano', 'Vivi', 'Jhair' , 'Eduardo']
p1, p2, p3, p4 = elementos
print(p1)

#asignar el resto de elementos a c usando *
a, b, *c = elementos
print(c)

#obviar el primer elemento y obtener el resto al final
_, b, *c = elementos
print(c)

print(elementos[:])

print(elementos[-1])

print(elementos[1:])

print(elementos[3:])

print(elementos[:2])

print(elementos[:3])

#agregar elementos a la lista
elementos.append('Ponwick')
print(elementos[:])

#insertar la posicion en el indice para agregar al elemento
elementos.insert(2, 'Thomas')
print(elementos)

#agregar mas de un elemento a la lista
elementos.extend(['Elemento adicional', 'Segundo Item adicional', 'ultimo elemento adicional'])
print(elementos)

print(elementos.index('Ponwick'))

#consultar si el elemento existe en la lista
print("Ponwick" in elementos)

#elemento con multiples tipos de datos
elemento_multiple = ['Ponsiano', 5, 5.60, True]
elemento_multiple.remove(5)
elemento_multiple.pop()
print(elemento_multiple)

#unir listas
unir_listas= elementos + elemento_multiple
print(unir_listas)