import random

var123 = ("papel", "piedra", "tijeras")

while True:
    users_pick = input("- Hola, bienvenido a Piedra, Papel o Tijeras. Por favor elige una opción: ")
    computer = random.choice(var123)

    if users_pick not in var123:
        print("¡Entrada no válida! Por favor elige solo entre:", var123)
    else:
        if users_pick == computer:
            print("Ambos eligieron", users_pick, ", es un empate.")
        elif users_pick == "tijeras":
            if computer == "piedra":
                print("La piedra aplasta las tijeras, has perdido.")
            else:
                print("Las tijeras cortan el papel, ¡has ganado!")
        elif users_pick == "piedra":
            if computer == "papel":
                print("El papel envuelve la piedra, has perdido.")
            else:
                print("La piedra aplasta las tijeras, ¡has ganado!")
        elif users_pick == "papel":
            if computer == "piedra":
                print("El papel envuelve la piedra, ¡has ganado!")
            else:
                print("Las tijeras cortan el papel, has perdido.")

    play_again = input("¿Quieres jugar otra vez? (si/no): ").lower()
    if play_again != "si":
        print("¡Gracias por jugar!")
        break