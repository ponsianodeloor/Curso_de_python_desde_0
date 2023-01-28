import sqlite3

cnn = sqlite3.connect("segunda_base")

mi_cursor = cnn.cursor()

mi_cursor.execute("""
    SELECT * FROM productos where seccion = 'Cursos PHP'
""")

productos = mi_cursor.fetchall()

for i in productos:
    print(i[1])

cnn.commit()
cnn.close()