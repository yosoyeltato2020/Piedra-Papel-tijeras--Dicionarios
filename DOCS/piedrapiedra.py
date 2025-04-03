

cantidad_partidas = 3

piedra = """  ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel = """ ___
---'   )
          ______)
          _______)
         _______)
---.__________)
"""
tijera = """ ___
---'   )
          ______)
       __________)
      (____)
---.__(___)
"""
lagarto = """
     ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
"""

spock = """
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


def mostrar_dibujo(opcion):
    dibujos = {1: piedra, 2: papel, 3: tijera, 4: lagarto, 5: spock}
    print(dibujos.get(opcion, "Opción inválida"))


def determinar_ganador(usuario1, usuario2):
    reglas = {
        1: [3, 4],  # piedra vence a tijera y lagarto
        2: [1, 5],  # papel vence a piedra y spock
        3: [2, 4],  # tijera vence a papel y lagarto
        4: [2, 5],  # lagarto vence a papel y spock
        5: [1, 3]   # spock vence a piedra y tijera
    }

    if usuario1 == usuario2:
        return "empate"
    elif usuario2 in reglas[usuario1]:
        return "usuario1"
    else:
        return "usuario2"


def jugar_maquina():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print("\n1. Piedra\n2. Papel\n3. Tijera\n4. Lagarto\n5. Spock")
        usuario = int(input("Introduce una opción: "))
        maquina = random.choice([1, 2, 3, 4, 5])

        print("\nTu elección:")
        mostrar_dibujo(usuario)
        print("Elección de la máquina:")
        mostrar_dibujo(maquina)

        resultado = determinar_ganador(usuario, maquina)

        if resultado == "usuario1":
            puntuacion1 += 1
            print("¡Ganaste esta ronda!")
        elif resultado == "usuario2":
            puntuacion2 += 1
            print("¡La máquina gana esta ronda!")
        else:
            print("Empate.")

        print(f"Puntuación: Tú {puntuacion1} - Máquina {puntuacion2}")

    if puntuacion1 > puntuacion2:
        print(f"\n¡Felicidades! Has ganado el mejor de {cantidad_partidas}.")
    else:
        print(f"\n¡La máquina gana el mejor de {cantidad_partidas}!")


def jugar_usuario():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print("\n1. Piedra\n2. Papel\n3. Tijera\n4. Lagarto\n5. Spock")
        usuario1 = int(input("Usuario 1, elige: "))
        usuario2 = int(input("Usuario 2, elige: "))

        print("\nUsuario 1 eligió:")
        mostrar_dibujo(usuario1)
        print("Usuario 2 eligió:")
        mostrar_dibujo(usuario2)

        resultado = determinar_ganador(usuario1, usuario2)

        if resultado == "usuario1":
            puntuacion1 += 1
            print("Usuario 1 gana esta ronda.")
        elif resultado == "usuario2":
            puntuacion2 += 1
            print("Usuario 2 gana esta ronda.")
        else:
            print("Empate.")

        print(f"Usuario1 - {puntuacion1} | Usuario2 - {puntuacion2}")

    if puntuacion1 > puntuacion2:
        print(f"\n¡Usuario 1 gana el mejor de {cantidad_partidas}!")
    else:
        print(f"\n¡Usuario 2 gana el mejor de {cantidad_partidas}!")
        

def main():
    print("Bienvenido al juego PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK")
    print("¿Contra quién quieres jugar? 1: Máquina | 2: Otro usuario")
    opcion = int(input("Introduce una opción 1 o 2: "))
    if opcion == 1:
        jugar_maquina()
    elif opcion == 2:
        jugar_usuario()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
    
    jugar_de_nuevo = input("¿Quieres volver a jugar? (s/n): ").lower()
    if jugar_de_nuevo == "s":
        main


main()
