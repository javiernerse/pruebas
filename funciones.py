from colorama import Fore,init,Back,Style
init(autoreset=True)


def imprime_menu() :
    imprime_amarillo("\t\t\t1) Crear Tabla  \n\t\t\t2) Agregar Datos \n\t\t\t3) Modificar Datos \n\t\t\t4) Ver Datos  \n\t\t\t5) Eliminar Datos  \n\t\t\t6) Salir\n\n")


def calc_iva (importe):
    iva = importe * 0.21
    total= importe + iva
    return importe, iva, total


def linea_verde ():
    ##from colorama import Fore,init
    ##init(autoreset=True)
    print(Fore.GREEN + "==================================================================")

def linea_negra ():
    ##from colorama import Fore,init
    ##init(autoreset=True)
    print(Fore.BLACK+ "==================================================================")    

def imprime_rojo (texto):
    ##from colorama import Fore,init
    ##init(autoreset=True)
    print(Fore.RED + texto)

def imprime_amarillo (texto):
    ##from colorama import Fore,init
    ##init(autoreset=True)
    print(Fore.YELLOW + texto)    

def imprime_azul(texto):
    ##from colorama import Fore,init
    ##init(autoreset=True)
    print(Fore.BLUE + texto) 

def imprime_verde(texto):
    ##from colorama import Fore,init
    ##init(autoreset=True)
    print(Fore.GREEN + texto)     
    
def imprime_cyan(texto):
    ##from colorama import Fore,init
    ##init(autoreset=True)
    print(Fore.CYAN + Back.LIGHTBLACK_EX + Style.BRIGHT + texto)    
 