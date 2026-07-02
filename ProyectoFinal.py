import sqlite3
import imprime_color
import funciones_BD


def imprime_menu() :
    imprime_color.linea_verde()
    imprime_color.imprime_amarillo("\t\t\t\t--- MENU ---\n")
    imprime_color.linea_verde()
    imprime_color.imprime_amarillo(
                             
                            "\t\t\t1. Agregar producto\n"
                            "\t\t\t2. Ver productos\n"
                            "\t\t\t3. Buscar por nombre\n"
                            "\t\t\t4. Eliminar producto\n"
                            "\t\t\t5. Actualizar precio\n"
                            "\t\t\t6. Buscar por categoria y precio\n"
                            "\t\t\t7. Salir")
    imprime_color.linea_verde()
    imprime_color.linea_verde()


    return input("Elegir opcion: ")

    
print("\n\n ")


flag_programa_on = False
funciones_BD.crear_tabla()

while(flag_programa_on == 0) :

                        resp=imprime_menu()

                        match resp: 
                            case "1": ## AGREGAR DATOS
                              flag_agregar_datos=False
                              while (flag_agregar_datos == 0):
                                            imprime_color.linea_verde()
                                            funciones_BD.agregar_datos()
                                            imprime_color.imprime_azul("Agrega otro dato ?(s/n) :")
                                            flag_fin_agregar=input()
                                            if (flag_fin_agregar == "n") or (flag_fin_agregar== "N"):
                                                   flag_agregar_datos = True
                                            else : flag_agregar_datos = False


                            case "2" :## VER PRODUCTOS
                                    
                                    imprime_color.linea_verde()
                                    imprime_color.imprime_amarillo("\t\t\t\tINGRESO DE DATOS")
                                   ## conexion = sqlite3.connect("productos.db")
                                    ##cursor=conexion.cursor()
                                    flag_insert=False
                                    while(flag_insert==0):
                                        ##imprime_color.imprime_azul("\t\t\tIngrese Producto : ")
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
                                    imprime_color.linea_verde()
                                    imprime_color.imprime_amarillo("\n\n\n\nModificar Datos")

                            case "4":## Ver datos
                                    imprime_color.linea_verde()
                                   ## conexion = sqlite3.connect("productos.db")
                                    ##cursor = conexion.cursor()
                                    # Recuperar todos los registros de la tabla productos
                                    cursor.execute('SELECT * FROM productos')
                                    productos = cursor.fetchall()
                                    print("\t\t\t=== Lista de Productos ===")
                                    for producto in productos:
                                        if (producto[0] % 2 == 0):
                                        ##print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio:${producto[2]:.2f}")
                                            imprime_color.imprime_amarillo(f"\t\t\tID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")
                                        else:
                                             imprime_color.imprime_cyan(f"\t\t\tID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")   
                                    imprime_color.linea_verde()

                                    
                                    
                                    # Cerrar la conexión
                                    ##conexion.close()  
                                    imprime_menu()          

                                                                            

                                                                               

                            case "7": 
                                    #conexion.close() 
                                    flag_programa_on=1

                                    imprime_color.imprime_rojo("SALIENDO . . . .")
