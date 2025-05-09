import random

opciones = ["piedra", "papel", "tijeras"]

while True:
    jugador = input("elige piedra, papel o tijeras (o'salir' para terminar)").lower()
    if jugador == "salir":
        print("Programa finalizado")
        break
    if jugador not in opciones:
        print("Opción inválida, intenta de nuevo.")
        continue

    computadora =random.choice(opciones)
    print(f"La computadora eligió:{computadora}")

    if jugador == computadora:
        print("¡Es un empate!")
    
    elif (jugador == "piedra" and computadora =="tijeras") or \
    (jugador == "papel" and computadora == "piedra") or \
    (jugador == "tijeras" and computadora == "papel"):
     print("Ganaste")
    else:
     print("Perdiste.")