print ("Bienvenido, este es un programa de subsidio al gasto de gas")
print ("recuerde escribir su numero de quintil(Ej: 1, 2, 3, 4, 5)")

quintil = int(input ("Cual es su quintil(1 a 5)? "))
labura = input ("Cual es su condicion laboral? (empleado, desempleado) ")
subsidio = 0

if (quintil == 1 or quintil == 2) and (labura == "desempleado" ):
    subsidio = 10000
    print ("su subsidio es de " ,subsidio)