import random

# Constantes y diccionarios
OPCIONES = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera",
    4: "Lagarto",
    5: "Spock"
}

REGLAS = {
    1: [3, 4],  # Piedra vence a Tijera y Lagarto
    2: [1, 5],  # Papel vence a Piedra y Spock
    3: [2, 4],  # Tijera vence a Papel y Lagarto
    4: [2, 5],  # Lagarto vence a Papel y Spock
    5: [1, 3]   # Spock vence a Piedra y Tijera
}

DIBUJOS = {
    1: """  ___\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n""",
    2: """ ___\n---'   )\n          ______)\n          _______)\n         _______)\n---.__________)\n""",
    3: """ ___\n---'   )\n          ______)\n       __________)\n      (____)\n---.__(___)\n""",
    4: """
     ___\n---'   __)__\n          ______)\n       __________)\n      (____)\n---.__(___)\n""",
    5: """
    ⌠⌒|
 ⌠⌒⌉| |   ◜﹆◜﹆
 | ||⩧|  / // /
 |_|| | /-//=/
 | || |/ // /
 ( || | // /
 |         .______
 |         __⫫____)
  |       |
"""
}

# Función para obtener la elección del usuario
def obtener_eleccion_usuario(mensaje):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in OPCIONES:
                return opcion
        except ValueError:
            pass
        print("Opción inválida. Inténtalo de nuevo.")

# Función para determinar el ganador
def determinar_ganador(j1, j2):
    if j1 == j2:
        return "Empate"
    return "Jugador 1 gana" if j2 in REGLAS[j1] else "Jugador 2 gana"

# Función para mostrar el dibujo
def mostrar_dibujo(opcion):
    print(DIBUJOS.get(opcion, "Opción inválida"))

# Función para jugar contra la máquina
def jugar_maquina():
    usuario = obtener_eleccion_usuario("Elige (1(piedra)- 2(papel)- 3(tijeras)- 4(lagarto)- 5 (spock): ")
    maquina = random.choice(list(OPCIONES.keys()))
    print(f"Elegiste {OPCIONES[usuario]}:")
    mostrar_dibujo(usuario)
    print(f"La máquina eligió {OPCIONES[maquina]}:")
    mostrar_dibujo(maquina)
    print(determinar_ganador(usuario, maquina))

# Función para jugar entre dos usuarios
def jugar_usuario():
    j1 = obtener_eleccion_usuario("Jugador 1 elige (1-5): ")
    j2 = obtener_eleccion_usuario("Jugador 2 elige (1-5): ")
    print(f"Jugador 1 eligió {OPCIONES[j1]}:")
    mostrar_dibujo(j1)
    print(f"Jugador 2 eligió {OPCIONES[j2]}:")
    mostrar_dibujo(j2)
    print(determinar_ganador(j1, j2))

# Función principal
def main():
    modo = obtener_eleccion_usuario("Jugar contra (1) Máquina o (2) Usuario: ")
    jugar_maquina() if modo == 1 else jugar_usuario()
    if input("¿Jugar de nuevo? (s/n): ").lower() == "s":
        main()

main()
