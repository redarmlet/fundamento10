"""
Desarolla un programa que genere un número aleatorio dentre de un rango definido por el usuario.
Luego dividirlo por cuatro
Luego, el usuario debería adivinar el número en un maximo de 3 intentos.
Condiciones del juego:

Ingreso de datos:
-A, El usuario debe ingresar numeros enteros para representar el rango numerico.
-B, El primer número debe ser menor que el segundo número.

Generación de número aleatorios:
-A, Se elige un numero aleatorio entre el rango definido por el usuario.
-B, El número aleatorio se divide por 4, y se redondea al multliplo de 4 más cercano. 

Intentos del usuario:
-A, Si el usuario acierta, se muestra un mensaje de felicitaciones.
-B, Si el usuario no acierta, se le indica si el número es mayor o menor.
-D, Resultado final: si no acierta en 3 intentos, se muestra el número aleatorio generado y se le indica que ha perdido.
"""

A=int(input("Ingrese el primer número: "))

B=int(input("Ingrese el segundo número: "))
while A > B:
    print("Por favor Ingrese un número válido. (Debe ser mayor que el primero.)")
    B = int(input("Segundo Número: "))

import random

Aleatorio= (random.randint(A,B))
guess = round(Aleatorio)
COUNT = 0

if COUNT == 0:
    number="primer"
if COUNT == 1:
    number="segundo"
if COUNT == 2:
    number ="tercer"


print("Ahora intente adivinar el número aleatorio escogido dentro del rango proporcionado.")
print("Haga su ",number," intento:")
TRY = int(input(""))




while COUNT < 2:


    if TRY < guess:
        print("Casi, ",TRY," es menor que el número aleatorio")
        COUNT = COUNT+1

        if COUNT == 0:
            number="primer"
        if COUNT == 1:
            number="segundo"
        elif COUNT == 2:
            number ="tercer"

        print("Haga su ",number," intento:")
        TRY = int(input(""))

    elif TRY > guess:
        print("Casi, ",TRY," es mayor que el número aleatorio")
        COUNT = COUNT+1
        
        if COUNT == 0:
            number="primer"
        if COUNT == 1:
            number="segundo"
        elif COUNT == 2:
            number ="tercer"
            
        print("Haga su ",number," intento:")
        TRY = int(input(""))
    else:
        print("Usted ha acertado, felicitaciones.")
        COUNT = COUNT+1

if TRY == guess:
    print("Excelente. Que tenga buen día")
else:
    print("Usted ha fracasado, más suerte a la próxima.")