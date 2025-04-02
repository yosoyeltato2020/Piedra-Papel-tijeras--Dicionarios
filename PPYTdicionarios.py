import random

# Diccionario de opciones
opciones = {
    'piedra': 0,
    'papel': 1,
    'tijeras': 2,
    'lagarto': 3,
    'spock': 4
}

# Diccionario de resultados
resultados = {
    (0, 2): "Piedra aplasta Tijeras",
    (0, 3): "Piedra aplasta Lagarto",
    (1, 0): "Papel cubre Piedra",
    (1, 4): "Papel refuta Spock",
    (2, 1): "Tijeras cortan Papel",
    (2, 3): "Tijeras decapitan Lagarto",
    (3, 1): "Lagarto devora Papel",
    (3, 4): "Lagarto envenena Spock",
    (4, 0): "Spock vaporiza Piedra",
    (4, 2): "Spock rompe Tijeras"
}

# Función para determinar el resultado de una ronda
def determinar_resultado(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (opciones[jugador1], opciones[jugador2]) in resultados:
        return f"Jugador 1 gana: {resultados[(opciones[jugador1], opciones[jugador2])]}"
    else:
        return f"Jugador 2 gana: {resultados[(opciones[jugador2], opciones[jugador1])]}"

# Función para jugar una partida al mejor de 5 rondas
def jugar_partida(modo):
    victorias_jugador1 = 0
    victorias_jugador2 = 0
    rondas_necesarias = 3

    print("¡Comienza la partida al mejor de 5 rondas!")

    while victorias_jugador1 < rondas_necesarias and victorias_jugador2 < rondas_necesarias:
        jugador1 = input("\nJugador 1, elige piedra, papel, tijeras, lagarto o spock: ").lower()
        if jugador1 not in opciones:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        if modo == '2':
            jugador2 = input("Jugador 2, elige piedra, papel, tijeras, lagarto o spock: ").lower()
            if jugador2 not in opciones:
                print("Opción no válida. Inténtalo de nuevo.")
                continue
        else:
            jugador2 = random.choice(list(opciones.keys()))
            print(f"La computadora eligió: {jugador2}")

        print(f"Jugador 1 eligió: {jugador1}")
        print(f"Jugador 2 eligió: {jugador2}")

        resultado = determinar_resultado(jugador1, jugador2)
        print(resultado)

        if resultado.startswith("Jugador 1 gana"):
            victorias_jugador1 += 1
        elif resultado.startswith("Jugador 2 gana"):
            victorias_jugador2 += 1

        print(f"Puntuación: Jugador 1 - {victorias_jugador1}, Jugador 2 - {victorias_jugador2}")

    if victorias_jugador1 == rondas_necesarias:
        print("\n¡Jugador 1 gana la partida!")
    else:
        print("\n¡Jugador 2 gana la partida!")

# Función principal que inicia el juego
def iniciar_juego():
    print("Bienvenido al juego de Piedra, Papel, Tijeras, Lagarto, Spock.")
    while True:
        modo = input("\nSelecciona el modo de juego: \n1. Contra la computadora\n2. Contra otro jugador\nElige 1 o 2: ")
        if modo not in ['1', '2']:
            print("Selección no válida. Inténtalo de nuevo.")
            continue

        jugar_partida(modo)
        jugar_nuevamente = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
        if jugar_nuevamente != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

# Ejecutar el juego
iniciar_juego()
