## MODULO PARA FUNCIONES DE CREAR TABLA


import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()
print("ejecutando database")

def crear_tabla():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL
    )
    """)

    conexion.commit()


def cerrar_conexion():

    conexion.close()