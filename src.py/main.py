from logic import determinar_resultado
from scoreboard import marcador, actualizar_marcador
from random_gen import jugada_computador
import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    usuario = input("Elige piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)

    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste...")

if __name__ == "__main__":
    jugar()
