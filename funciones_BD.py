## MODULO PARA FUNCIONES DE CREAR TABLA


import sqlite3




def validar_precio(texto):
    
    try:

        precio = float(texto)

    except ValueError:

        raise ValueError(
            "El precio debe contener solo números"
        )

    if precio < 0:

        raise ValueError(
            "El precio no puede ser negativo"
        )

    return precio


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



def agregar_datos():
    nombre = input("Nombre: ").strip()
    categoria = input("Categoria: ").strip()
    precio_texto = input("Precio: ").strip()

    if not nombre:

        print("Nombre inválido")
        return

    if not categoria:

        print("Categoría inválida")
        return

    try:

        precio = validar_precio(precio_texto)

    except ValueError as error:

        print(error)
        return

    cursor.execute(
        """
        INSERT INTO productos(nombre,categoria,precio)
        VALUES(?,?,?)
        """,
        (nombre, categoria, precio)
    )

    conexion.commit()

    print("Producto agregado")    
