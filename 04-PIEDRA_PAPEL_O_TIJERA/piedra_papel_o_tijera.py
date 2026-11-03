import random

print("Juguemos piedra papel o tijera")

eleccion_jugador = input("\n Piedra, papel o tijera?: ").lower()

elecciones = ["piedra", "papel", "tijera"]
elecccion_pc = random.choice(elecciones)

print(f"Has elegido: {eleccion_jugador}")
print(f"la pc eligio: {elecccion_pc}")

if (eleccion_jugador == "piedra" and elecccion_pc == "tijera") or (eleccion_jugador == "papel" and elecccion_pc == "piedra") or (eleccion_jugador == "tijera" and elecccion_pc == "papel"):
    print("Has ganado")
elif (eleccion_jugador == "piedra" and elecccion_pc == "papel") or (eleccion_jugador == "papel" and elecccion_pc == "tijera") or (eleccion_jugador == "tijera" and elecccion_pc == "piedra"):
    print("Has perdiddo")
else:
    print("empate")