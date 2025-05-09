"""
Necesitamos generar un programa en python que permita adivinar 3 números aleatorios dentro
del rango definido por el usuario y ajustarlos dividiéndolos entre 4
luego el usuario debe dar un número para luego dividirlo nuevamente entre un máximo
de 3 intentos.

Condiciones:

1: Ingreso de datos:
a: el usuario ingresa 2 números enteros que representan el rango numérico
b: el primer número debe ser menor que el segundo

2: generación del número aleatorio:
a: si se eligiese un número aleatorio dentro del rango ingresado
b: el número se ajusta dividiéndolo entre 4 y redondeándolo al múltiplo de 4 más cercano

3: Intento del usuario: a: primer intento, si el usuario acierta se le muestra felicitaciones, adivinaste al primer intento
b: segundo intento, si el usuario no acierta se le indicará si el número es mayor o menor
c: tercer intento, si no acierta se le devuelve una pista d: resultado final: si no acierta en los 3 intentos el programa muestra
el mensaje "perdiste, el número es incorrecto"
"""

import random
A = int(input("Ingrese el primer número: "))
B = int(input("Ingrese el segundo número: "))

C = random.randint(A, B)
D = C/4
print("C Y D SON RESPECTIVAMENTE: ", C, D)