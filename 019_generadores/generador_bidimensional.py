def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for sub_elemento in elemento:
            yield sub_elemento

ciudades_devueltas = devuelveCiudades("Madrid", "Barcelona", "Valencia", "Bilbao")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
        #for sub_elemento in elemento:
            yield from elemento

ciudades_devueltas = devuelveCiudades2("Madrid", "Barcelona", "Valencia", "Bilbao")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))