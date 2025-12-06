from logic import determinar_ganador
from random_gen import jugada_computadora
from scoreboard import Scoreboard

def jugar():
    marcador = Scoreboard()

    while True:
        usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
        if usuario == "salir":
            print("Juego terminado.")
            marcador.mostrar()
            break

        computadora = jugada_computadora()
        print(f"Tú elegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(usuario, computadora)

        if resultado == "empate":
            print("¡Empate!")
        elif resultado == "usuario":
            print("¡Ganaste!")
        else:
            print("Perdiste...")

        marcador.actualizar(resultado)
        marcador.mostrar()

if __name__ == "__main__":
    jugar()
