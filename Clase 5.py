"""
Una tienda de perfumes llamada Gloria
El representate de la tienda necesita organizar el formulario de ventas, y él piensa que representando el siguiente formulario, podría mejorar sus ventas.
ya que el formulario tiene 10 ítems para atender al usuario.
A continuación los cargos que el gerente desea implementar.
1 numero de boleta
2 numero de identificación
3 nombre del cliente
4 productos del pedido
"""

a = """
 1- Perfume Organza para Damas
 2- Katty Perry para damas
 3- Mañana Fresca para damas
 4- La mejor noche para damas
 5- Sueño exclusivo para damas

 6- Ahora si voy for male
 7- Antonio banderas for male
 8- Lacoste for male
 9- Hugo boss Red for male
 10- A que te quito el sueño for male
"""

"""Los de 50 ml tienen un precio de $10000
Los de 100ml tienen un precio de $18000

Añadir el pedido
Sacar el total
Sacar el IVA. (19%)
"""

print ("Bienvenido a la casa de perfumes Gloria")
nombre = input("Ingrese su nombre: ")
print ("Bienvenido",nombre,)
RUT = input("Ingrese su RUT: ")
print (nombre, ", su identifiación se ha validado correctamente")
print("  ")
print ("A continuación se muestra el catálogo, elija el numero del producto que desee agregar a la orden")

lista=[]

print(a)
elect = input()


if elect == 1 :
    lista.append("Perfume Organza para Damas")
    
    print("Opción 1")
elif elect == 2:
    lista.append("Katty Perry para Damas")
    
    
    print("Opción 2")
elif elect == 3:
    lista.append("Mañana fresca para damas")
    
    print("Opción 3")
elif elect == 4:
    lista.append("La mejor noche para damas")
    
    print("Opción 4")
elif elect == 5:
    lista.append("Sueño exclusivo para damas")
    
    print("Opción 5")
elif elect == 6:
    lista.append("Ahora si voy for male")
    
    print("Opción 6")
elif elect == 7:
    lista.append("Antonio banderas for male")
    
    print("Opción 7")
elif elect == 8:
    lista.append("Lacoste for male")
    
    print("Opción 8")
elif elect == 9:
    lista.append("Hugo Boss Red for male")
    
    print("Opción 9")
elif elect == 10:
    lista.append("A que te quito el sueño for male")
    
    print("Opción 10")
else:
    print("escoja una opción válida")
