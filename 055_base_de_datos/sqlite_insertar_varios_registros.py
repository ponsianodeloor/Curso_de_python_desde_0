import sqlite3

#se especifica el nombre de la base de datos
cnn = sqlite3.connect("primera_base")

#crear puntero
mi_cursor = cnn.cursor()

#ejecutar consulta para crear una tabla
# se la comenta ya que la tabla esta creada
#mi_cursor.execute("CREATE TABLE products(name VARCHAR(50), price INTEGER, section VARCHAR(20))")

#uso de una tupla
varios_productos = [
    ("Curso de Laravel", 120, "Cursos PHP"),
    ("Curso de Java", 120, "Cursos Java"),
    ("Curso de Django", 120, "Cursos Python"),
]

mi_cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", varios_productos)
cnn.commit()

cnn.close()