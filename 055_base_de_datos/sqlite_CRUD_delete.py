import sqlite3

cnn = sqlite3.connect("segunda_base")

mi_cursor = cnn.cursor()

mi_cursor.execute("""
    DELETE from productos WHERE id = 2
""")

cnn.commit()
cnn.close()