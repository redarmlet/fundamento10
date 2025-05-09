"""
# Desarrolle un programa en Python que permita calcular el subsidio de gas según el quintil de ingreso al que pertenece la familia del solicitante y sus condiciones laborales.

# Condiciones socioeconómicas:
# 1. Menor Ingreso
# 2. Mayor Ingreso

# Condiciones laborales:
# 1. Se considera si la persona está empleada o desempleada.

# Condiciones de subsidio:
# 1. Gas

# Quintil: 1 o 2, Laboral: Desempleado, Subsidio: 10.000
# Quintil: 1 o 2, Laboral: Empleado, Subsidio: 8.000
# Quintil: 3, Laboral: Desempleado, Subsidio: 6.000
# Quintil: 3, Laboral: Empleado, Subsidio: 4.000
# Quintil: 4 o 5, Laboral: Cualquiera, Subsidio: 1.500

# Bonos adicionales:
# Si la persona pertenece al quintil 1 o 2, recibe un bono de 2.000, y si tiene más de 65 años, recibe un bono de 3.000.
"""
A="""
(1)Para Quintil uno
(2)Para Quintil dos
(3)Para Quintil tres
(4)Para Quintil cuatro
(5)Para Quintil cinco
"""
print("Bienvenido a la calculadora de Subsidio al consumo de gas.")
print("Recuerde que: ")
print(A)
quintil=int(input("Ingrese el quintil al que pertenece: "))
print(" ")
empleo=input("Ingrese (si) o (no), para indicar si actualmente tiene empleo: ")
print(" ")


if (quintil == 1 or quintil == 2) and (empleo == "no"):
    print("Usted tiene un subsidio de $10000")
    subsidio = 12000
    print("Además por ser del quintil 1 o 2, usted recibe un subsidio extra de $2000")
if (quintil == 1 or quintil == 2) and empleo == "si":
    print("Usted tiene un subsidio de $8000")
    subsidio = 10000
    print("Además por ser del quintil 1 o 2, usted recibe un subsidio extra de $2000")
if quintil == 3 and empleo == "no":
    print("Usted tiene un subsidio de $6000")
    subsidio = 6000
if quintil == 3 and empleo == "si":
    print("Usted tiene un subsidio de $4000")
    subsidio = 4000
if (quintil == 4 or quintil == 5) and (empleo == "si" or "no"):
    print("Usted tiene un subsidio de $1500")
    subsidio = 1500
else:
    print("")

edad = int(input("Por favor ingrese su edad: "))

if edad >= 65:
    print("Por su edad, usted recibe un Bono de $3000 extra.")
    subsidio = subsidio+3000
elif edad < 65:
    print(" ")
else:
    print("")
print(" ")
print("Su subsidio final sería de: $",subsidio)
print("Que tenga buen día.")