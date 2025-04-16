"""
Realizar un menú que presente las siguientes opciones al usuario;
Un saludo al colocar el número uno
Una despedida al presionar el número dos
Una edad 
Else "opcion invalida"
"""

a="""
Bienvenido, Escoja una de las siguientes opciones:
(1)Saludo Aleatorio
(2)Despedida Aleatoria
(3)Edad Aleatoria

[Recuerde escribir el número de la opción deseada :)]
"""
print (a)
import random

elect = input(" ")

if elect == "1":
    saludo=["¡Hola!", "¿Qué tal?", "¡Buenos días!", "¡Buenas tardes!", "¡Buenas noches!", "¡Cómo estás?", "¡Qué onda!", "¡Qué hay!", "¡Hola, ¿cómo vas?", "¡Qué pasa!", "¡Qué tal todo!", "¡Mucho gusto!", "¡Qué tal, cómo te va?", "¡Qué gusto verte!", "¡Saludos!"]

    print(random.choice(saludo))
elif elect == "2":
    despedida=["¡Adiós!", "¡Hasta luego!", "¡Nos vemos!", "¡Cuídate!", "¡Hasta pronto!", "¡Que tengas un buen día!", "¡Hasta la próxima!", "¡Chao!", "¡Nos estamos viendo!", "¡Que te vaya bien!", "¡Hasta luego, cuídate!", "¡Adiós, que estés bien!", "¡Que tengas un excelente día!", "¡Nos vemos pronto!"]

    print(random.choice(despedida))
elif elect == "3":
    edad = random.randint(1, 100)
    
    print("Se ha escogido aleatoriamente la edad de: ",edad," años")
else:
    
    print("Opción inválida")