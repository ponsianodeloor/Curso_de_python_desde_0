import sqlite3

#se especifica el nombre de la base de datos
cnn = sqlite3.connect("primera_base")

#crear puntero
mi_cursor = cnn.cursor()

#ejecutar consulta para crear una tabla
# se la comenta ya que la tabla esta creada
#mi_cursor.execute("CREATE TABLE products(name VARCHAR(50), price INTEGER, section VARCHAR(20))")

mi_cursor.execute("SELECT * FROM products")
listado_productos = mi_cursor.fetchall()

#este comando sirve para realizar los cambios de las instrucciones
cnn.commit()

for c in listado_productos:
    print(c[0])

print(listado_productos)


cnn.close()