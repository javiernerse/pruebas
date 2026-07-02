from colorama import Fore,init,Back,Style
init(autoreset=True)





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
 