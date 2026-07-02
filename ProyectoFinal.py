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
                                            # Llamado a la funcion para agregar datos
                                            funciones_BD.agregar_datos()
                                            imprime_color.imprime_azul("Agrega otro dato ?(s/n) :")
                                            flag_fin_agregar=input()
                                            if (flag_fin_agregar == "n") or (flag_fin_agregar== "N"):
                                                   flag_agregar_datos = True
                                            else : flag_agregar_datos = False


                            case "2": ## VER PRODUCTOS
                                        imprime_color.linea_verde()
                                        funciones_BD.ver_productos()

                                    
                                    


                            case "3": ##Buscar por nombre\n"         
                                    imprime_color.linea_verde()
                                    imprime_color.imprime_amarillo("\n\n\n\n")

                            case "4":## Ver datos
                                    

                                                                            

                                                                               

                            case "7": 
                                    #conexion.close() 
                                    flag_programa_on=1

                                    imprime_color.imprime_rojo("SALIENDO . . . .")
