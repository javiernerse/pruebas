## MODULO PARA FUNCIONES DE CREAR TABLA


import sqlite3
import imprime_color




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
        INSERT INTO inventario(nombre,categoria,precio)
        VALUES(?,?,?)
        """,
        (nombre, categoria, precio)
    )

    conexion.commit()

    print("Producto agregado")    


def ver_productos():

    cursor.execute("SELECT * FROM inventario")

    productos = cursor.fetchall()

    if len(productos) == 0:

        print("No hay productos")
        return
    #Recordemos que el enumerate devuelve una tupla
    #Siendo (indice/enumeracion, objeto)
    #lista_productos = cursor.fetchall()
    print("\t\t\t=== Lista de Productos ===")
    for producto in productos:

        id_prod = f"ID: {producto[0]}"
        nombre_prod = f"Nombre: {producto[1]}"
        categoria_prod = f"Categoria: {producto[2]}"
        precio_prod = f"Precio: $ {producto[3]:.2f}"
        
        # Formateamos con anchos fijos (:<15 significa alineado a la izquierda, ocupando 15 caracteres)
        linea_formateada = f"\t\t\t{id_prod:<8} {nombre_prod:<22} {categoria_prod:<22} {precio_prod}"
        
        # Imprimimos según si el ID es par o impar
        if producto[0] % 2 == 0:
            imprime_color.imprime_amarillo(linea_formateada)
        else:
            imprime_color.imprime_cyan(linea_formateada)
       # if (producto[0] % 2 == 0):
                                        
        #    imprime_color.imprime_amarillo(f"\t\t\tID: {producto[0]}\tNombre: {producto[1]}\tCategoria: {producto[2]}\tPrecio: $ {producto[3]:.2f}")
       # else:
        #    imprime_color.imprime_cyan(f"\t\t\tID: {producto[0]}\tNombre: {producto[1]}\tCategoria: {producto[2]}\tPrecio: $ {producto[3]:.2f}")   

    imprime_color.linea_verde()
        