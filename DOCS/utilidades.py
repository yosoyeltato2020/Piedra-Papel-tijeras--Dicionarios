### Archivo: utilidades.py

# Colores ANSI
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

piedra = f"""{BLUE}  ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___){RESET}
"""

papel = f"""{YELLOW} ___
---'   )
          ______)
          _______)
         _______)
---.__________){RESET}
"""

tijera = f"""{RED} ___
---'   )
          ______)
       __________)
      (____)
---.__(___){RESET}
"""

lagarto = f"""{MAGENTA}
     ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___){RESET}
"""

spock = f"""{CYAN}
    \u2320\u02d8|
 \u2320\u02d8\u2313| |   \u02dc\u2575\u02dc\u2575
 | ||\u2a67|  / // /
 |_|| | /-//=/
 | || |/ // /
 ( || | // /
 |         .______
 |         __\u2b2b____)
  |       |
{RESET}"""

opciones = {1: piedra, 2: papel, 3: tijera, 4: lagarto, 5: spock}

def mostrar_dibujo(opcion):
    print(opciones.get(opcion, f"{RED}Opción inválida{RESET}"))

def determinar_ganador(usuario1, usuario2):
    reglas = {
        1: [3, 4],  # piedra vence a tijera y lagarto
        2: [1, 5],  # papel vence a piedra y spock
        3: [2, 4],  # tijera vence a papel y lagarto
        4: [2, 5],  # lagarto vence a papel y spock
        5: [1, 3]   # spock vence a piedra y tijera
    }

    if usuario1 == usuario2:
        return f"{YELLOW}Empate{RESET}"
    elif usuario2 in reglas[usuario1]:
        return "usuario1"
    else:
        return "usuario2"