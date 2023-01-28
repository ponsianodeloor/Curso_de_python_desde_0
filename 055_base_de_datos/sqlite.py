import sqlite3

#se especifica el nombre de la base de datos
cnn = sqlite3.connect("primera_base")

#crear puntero
mi_cursor = cnn.cursor()

#ejecutar consulta para crear una tabla
# se la comenta ya que la tabla esta creada
#mi_cursor.execute("CREATE TABLE products(name VARCHAR(50), price INTEGER, section VARCHAR(20))")

mi_cursor.execute("INSERT INTO products(name, price, section) VALUES ('Curso de Python', 50, 'Cursos Informaticos')")

#este comando sirve para realizar los cambios de las instrucciones
cnn.commit()

cnn.close()