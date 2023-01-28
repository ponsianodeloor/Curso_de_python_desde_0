import sqlite3

cnn = sqlite3.connect("segunda_base")

mi_cursor = cnn.cursor()

#codigo_articulo VARCHAR(4) PRIMARY KEY,
mi_cursor.execute("""
    CREATE TABLE productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,        
        nombre_articulo VARCHAR(50), 
        precio INTEGER,
        seccion VARCHAR(20)
    )
""")

varios_productos = [
    ("Curso de Laravel", 120, "Cursos PHP"),
    ("Curso de Java", 130, "Cursos Java"),
    ("Curso de Django", 140, "Cursos Python"),
]

mi_cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", varios_productos)

cnn.commit()
cnn.close()