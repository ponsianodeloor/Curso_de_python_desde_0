print("Asignaturas optativas Año 2023")

print("Asignaturas disponibles:")

asignaturas={1:"Informática gráfica",2:"Pruebas de Software",3:"Usabilidad y Accesabilidad"}

print("1.- Informática Gráfica.")
print("2.- Pruebas de software")
print("3.- Usabilidad y accesabilidad")

eleccion=int(input("Digita el número de la asignatura escogida: "))

if eleccion in (1,2,3):
 print("La asignatura escogida es "+ asignaturas[eleccion])
else:
 print("La asignatura escogida no está disponible.")