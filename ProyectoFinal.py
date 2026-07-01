import sqlite3
import funciones


def imprime_menu() :
    funciones.linea_verde()
    funciones.linea_verde()
    funciones.imprime_amarillo("\t\t\t1) Crear Tabla  \
                               \n\t\t\t2) Agregar Datos  \
                               \n\t\t\t3) Modificar Datos  \
                               \n\t\t\t4) Ver Datos   \
                               \n\t\t\t5) Eliminar Datos  \
                               \n\t\t\t6) Salir\n")
    funciones.linea_verde()
    funciones.linea_verde()

print("\n\n ")

imprime_menu()
flag_programa_on = False
conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

while(flag_programa_on == 0) :

                        resp=input("\t\t\t")

                        match resp: 
                            case "1": 
                            ##nombre_tabla=input("Ingrese nombre tabla :")
                                   ## conexion = sqlite3.connect("productos.db")
                                    ##cursor = conexion.cursor()
                             # Crear una tabla
                                    cursor.execute('''CREATE TABLE IF NOT EXISTS inventario (
                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    Nombre TEXT NOT NULL,
                                                   Descripcion TEXT,
                                                   Cantidad INT NOT NULL,

                                                    precio REAL NOT NULL,
                                                   Categoria TEXT
                                                     )
                                                    ''')
                                    ##conexion.close()
                                    funciones.imprime_verde("\t\t\tTABLA CREADA")
                                    imprime_menu()


                            case "2" :
                                    funciones.linea_verde()
                                    funciones.imprime_amarillo("\t\t\t\tINGRESO DE DATOS")
                                   ## conexion = sqlite3.connect("productos.db")
                                    ##cursor=conexion.cursor()
                                    flag_insert=False
                                    while(flag_insert==0):
                                        ##funciones.imprime_azul("\t\t\tIngrese Producto : ")
                                        aux_producto =input("\t\t\tIngrese Nombre del Producto : ")
                                        aux_descripcion=input("\t\t\tIngrese Descripcion :")
                                        aux_cantidad=int(input("\t\t\tIngrese cantidad :"))
                                        precio=float(input("\n\t\t\tIngrese Precio : "))
                                        aux_categoria=input("\t\t\tIngrese Categoria:")

                                       
                                       
                                       
                                        cursor.execute('''
                                                         INSERT INTO productos (nombre, precio) VALUES (?, ?)''', (aux_producto, precio))
                                        conexion.commit()
                                        resp_1=input(("AGREGA OTRO DATO ? (S/N)"))
                                        if ( resp_1=="n") or (resp_1=="N") :
                                                                            flag_insert=1
                                                                            
                                                                            break
                                        
                                    
                                    ##conexion.close()
                                    imprime_menu()


                            case "3": ##Modificar Datos            
                                    funciones.linea_verde()
                                    funciones.imprime_amarillo("\n\n\n\nModificar Datos")

                            case "4":## Ver datos
                                    funciones.linea_verde()
                                   ## conexion = sqlite3.connect("productos.db")
                                    ##cursor = conexion.cursor()
                                    # Recuperar todos los registros de la tabla productos
                                    cursor.execute('SELECT * FROM productos')
                                    productos = cursor.fetchall()
                                    print("\t\t\t=== Lista de Productos ===")
                                    for producto in productos:
                                        if (producto[0] % 2 == 0):
                                        ##print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio:${producto[2]:.2f}")
                                            funciones.imprime_amarillo(f"\t\t\tID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")
                                        else:
                                             funciones.imprime_cyan(f"\t\t\tID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")   
                                    funciones.linea_verde()

                                    
                                    
                                    # Cerrar la conexión
                                    ##conexion.close()  
                                    imprime_menu()          

                                                                            

                                                                               

                            case "6": 
                                    conexion.close() 
                                    flag_programa_on=1

                                    funciones.imprime_rojo("SALIENDO . . . .")
