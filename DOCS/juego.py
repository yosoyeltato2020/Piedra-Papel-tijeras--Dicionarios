## Archivo: juego.py
import random
from utilidades import *

cantidad_partidas = 3

opciones = {1: "Piedra", 2: "Papel", 3: "Tijera", 4: "Lagarto", 5: "Spock"}

def jugar_maquina():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print(f"\n{CYAN}1. Piedra\n2. Papel\n3. Tijera\n4. Lagarto\n5. Spock{RESET}")
        usuario = int(input("Introduce una opción: "))
        maquina = random.choice([1, 2, 3, 4, 5])

        print(f"\nTu elección: {opciones[usuario]}")
        mostrar_dibujo(usuario)
        print(f"Elección de la máquina: {opciones[maquina]}")
        mostrar_dibujo(maquina)

        resultado = determinar_ganador(usuario, maquina)

        if resultado == "usuario1":
            puntuacion1 += 1
            print(f"{GREEN}¡Ganaste esta ronda!{RESET}")
        elif resultado == "usuario2":
            puntuacion2 += 1
            print(f"{RED}¡La máquina gana esta ronda!{RESET}")
        else:
            print(f"{YELLOW}Empate.{RESET}")

        print(f"{CYAN}Puntuación: Tú {puntuacion1} - Máquina {puntuacion2}{RESET}")

    if puntuacion1 > puntuacion2:
        print(f"\n{GREEN}¡Felicidades! Has ganado el mejor de {cantidad_partidas}.{RESET}")
    else:
        print(f"\n{RED}¡La máquina gana el mejor de {cantidad_partidas}!{RESET}")

def jugar_usuario():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print(f"\n{CYAN}1. Piedra\n2. Papel\n3. Tijera\n4. Lagarto\n5. Spock{RESET}")
        usuario1 = int(input("Usuario 1, elige: "))
        usuario2 = int(input("Usuario 2, elige: "))

        print(f"\nUsuario 1 eligió: {opciones[usuario1]}")
        mostrar_dibujo(usuario1)
        print(f"Usuario 2 eligió: {opciones[usuario2]}")
        mostrar_dibujo(usuario2)

        resultado = determinar_ganador(usuario1, usuario2)

        if resultado == "usuario1":
            puntuacion1 += 1
            print(f"{GREEN}Usuario 1 gana esta ronda.{RESET}")
        elif resultado == "usuario2":
            puntuacion2 += 1
            print(f"{RED}Usuario 2 gana esta ronda.{RESET}")
        else:
            print(f"{YELLOW}Empate.{RESET}")

        print(f"{CYAN}Usuario1 - {puntuacion1} | Usuario2 - {puntuacion2}{RESET}")

    if puntuacion1 > puntuacion2:
        print(f"\n{GREEN}¡Usuario 1 gana el mejor de {cantidad_partidas}!{RESET}")
    else:
        print(f"\n{RED}¡Usuario 2 gana el mejor de {cantidad_partidas}!{RESET}")
