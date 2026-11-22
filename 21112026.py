"""
Nombre: Marco Adel Lopez Angulo
Fecha: 21/11/2026

Dentro de unos momentos procedere a estudiar las funciones, y de igual manera el reestructurar lo ejemplos previamente realizados como funciones
"""

import random

### Funciones ### 


'''
Esto es un bloque de codigo al cual se le asigna un nombre el cual realiza una tarea especifica.

Esto nos permite el reutilizar codigo, modularizarlo y estructurarlo de una manera mas manejable.

'''


def funcion_suma(X:int, Y:int): ### Definimos la funcion, con los parametros que requiere
    print(X + Y) ### La funcion imprime el cuerpo de la funcion

funcion_suma(34,55) ### Al llamar la funcion, va a requerir los parametros necesario para correr

### Parametros ### 

"""
Estos son argumentso, los cuales son valores que se pasan por la funcion desde fuera, lo cual puede ser recibido por la funcion para usar y procesar

Los parametros son los inputs que puede recibir la funcion.

El concepto de argumento y parametro estan muy relacionados. Pero estos no son exactamente los mismo, 

Los parametros son variablers que define la funcion
Los argumentos son los valores concretos que pasamos a la funcion

Dentro de las funciones no se deberian de pasar un numero excesivo de parametros.
"""

### Return ###

""" 
Son un resultado que se puede devolver desde una funcion de manera opcional.

El valor de RETURN devuelve el valor que obtiene la funcion, sin importar el tipo de dato que sea.

"""
mano = ["Piedra", "Papel", "Tijera"]




def Computadora():
    return random.choice(mano)

def Jugador():
    return random.choice(mano)


def Juego(computadora, jugador):
    if computadora == jugador:
        print("Empate")
    elif computadora == "Piedra" and jugador == "Papel":
        print("Gana el jugador: Papel envuelve Piedra")
    elif computadora == "Piedra" and jugador == "Tijeras":
        print("Gana la computadora: Piedra rompe Tijeras")
    elif computadora == "Papel" and jugador == "Piedra":
        print("Gana la computadora: Papel envuelve Piedra")
    elif computadora == "Papel" and jugador == "Tijeras":
        print("Gana el jugador: Tijeras corta Papel")
    elif computadora == "Tijeras" and jugador == "Piedra":
        print("Gana el jugador: Piedra rompe Tijeras")
    elif computadora == "Tijeras" and jugador == "Papel":
        print("Gana la computadora: Tijeras corta Papel")


Juego(Computadora(), Jugador())