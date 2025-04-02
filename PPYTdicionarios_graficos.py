from graphics import *
import random

# Diccionario de opciones y sus representaciones numéricas
opciones = {
    'piedra': 0,
    'papel': 1,
    'tijeras': 2,
    'lagarto': 3,
    'spock': 4
}

# Diccionario que define los resultados posibles
resultados = {
    (0, 2): "Ganado",  # Piedra aplasta Tijeras
    (0, 3): "Ganado",  # Piedra aplasta Lagarto
    (1, 0): "Ganado",  # Papel cubre Piedra
    (1, 4): "Ganado",  # Papel refuta Spock
    (2, 1): "Ganado",  # Tijeras cortan Papel
    (2, 3): "Ganado",  # Tijeras decapitan Lagarto
    (3, 1): "Ganado",  # Lagarto devora Papel
    (3, 4): "Ganado",  # Lagarto envenena Spock
    (4, 0): "Ganado",  # Spock vaporiza Piedra
    (4, 2): "Ganado",  # Spock rompe Tijeras
}

# Función para determinar el resultado de una ronda
def determinar_resultado(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (opciones[jugador], opciones[computadora]) in resultados:
        return "Ganado"
    else:
        return "Perdido"

# Función para manejar la selección del jugador y actualizar el mensaje y los puntajes
def seleccionar_opcion(opcion, mensaje, puntajes):
    computadora = random.choice(list(opciones.keys()))
    resultado = determinar_resultado(opcion, computadora)
    
    if resultado == "Ganado":
        puntajes['jugador'] += 1
    elif resultado == "Perdido":
        puntajes['computadora'] += 1

    mensaje.setText(f"Jugador: {opcion.capitalize()}\nComputadora: {computadora.capitalize()}\nResultado: {resultado}\n\nPuntuación - Jugador: {puntajes['jugador']} | Computadora: {puntajes['computadora']}")

# Función para crear la ventana del juego y manejar las interacciones
def crear_ventana():
    # Crear la ventana
    ventana = GraphWin("Piedra, Papel, Tijeras, Lagarto, Spock", 600, 400)
    ventana.setBackground("lightgray")
    
    # Título del juego
    titulo = Text(Point(300, 30), "Piedra, Papel, Tijeras, Lagarto, Spock")
    titulo.setSize(18)
    titulo.draw(ventana)

    # Mensaje para mostrar resultados y puntajes
    mensaje = Text(Point(300, 300), "Haz tu selección:")
    mensaje.setSize(14)
    mensaje.setTextColor("black")
    mensaje.draw(ventana)

    # Crear botones para cada opción del juego
    botones = []
    opciones_texto = ['Piedra', 'Papel', 'Tijeras', 'Lagarto', 'Spock']
    for i, opcion in enumerate(opciones_texto):
        boton = Rectangle(Point(100 + i*100, 100), Point(180 + i*100, 150))
        boton.setFill("lightblue")
        boton.draw(ventana)
        texto = Text(Point(140 + i*100, 125), opcion)
        texto.setSize(12)
        texto.draw(ventana)
        botones.append((boton, opcion.lower()))
    
    # Botón para salir del juego
    boton_salir = Rectangle(Point(250, 200), Point(350, 250))
    boton_salir.setFill("red")
    boton_salir.draw(ventana)
    texto_salir = Text(Point(300, 225), "Salir")
    texto_salir.setSize(12)
    texto_salir.draw(ventana)

    # Inicializar puntajes
    puntajes = {'jugador': 0, 'computadora': 0}

    # Bucle principal del juego
    while puntajes['jugador'] < 3 and puntajes['computadora'] < 3:
        clic = ventana.getMouse()
        if boton_salir.getP1().getX() < clic.getX() < boton_salir.getP2().getX() and boton_salir.getP1().getY() < clic.getY() < boton_salir.getP2().getY():
            ventana.close()
            return
        for boton, opcion in botones:
            if boton.getP1().getX() < clic.getX() < boton.getP2().getX() and boton.getP1().getY() < clic.getY() < boton.getP2().getY():
                seleccionar_opcion(opcion, mensaje, puntajes)
                break

    # Mostrar mensaje final con el ganador
    if puntajes['jugador'] == 3:
        mensaje.setText("¡Felicidades! Has ganado la partida.\nHaz clic en 'Salir' para cerrar el juego.")
    else:
        mensaje.setText("La computadora ha ganado la partida.\nHaz clic en 'Salir' para cerrar el juego.")

    # Esperar a que el jugador haga clic en 'Salir' para cerrar la ventana
    while True:
        clic = ventana.getMouse()
        if boton_salir.getP1().getX() < clic.getX() < boton_salir.getP2().getX() and boton_salir.getP1().getY() < clic.getY() < boton_salir.getP2().getY():
            break

    ventana.close()

# Ejecutar el juego
crear_ventana()
