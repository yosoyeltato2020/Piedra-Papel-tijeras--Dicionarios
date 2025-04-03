


### Archivo: main.py

from juego import jugar_maquina, jugar_usuario
from utilidades import *

def main():
    print(f"{CYAN}Bienvenido al juego PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK{RESET}")
    print(f"{YELLOW}¿Contra quién quieres jugar? 1: Máquina | 2: Otro usuario{RESET}")
    opcion = int(input("Introduce una opción 1 o 2: "))
    if opcion == 1:
        jugar_maquina()
    elif opcion == 2:
        jugar_usuario()
    else:
        print(f"{RED}Opción no válida. Inténtalo de nuevo.{RESET}")
    
    jugar_de_nuevo = input(f"{YELLOW}¿Quieres volver a jugar? (s/n):{RESET} ").lower()
    if jugar_de_nuevo == "s":
        main()

if __name__ == "__main__":
    main()
