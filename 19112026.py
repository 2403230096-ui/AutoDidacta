'''
Nombre: Marco Adel Lopez Angulo
Fecha: 17/11/2026

Dentro del archivo del dia de hoy se va a dar el enfoque dentro de lo que serian el proceso de ciclos dentro de la programacion.
Como es que estos funcionan dentro de la programacion y de igual manera como se pueden usar correctamente dentro de cualquier ambito.

Los bucles son estructuras de control que permiten repetir un conjunto de instrucciones varias veces.

'''

### WHILE ###

'''
Es una estructura de control que repite un bloque de codigo mientras una condicion se evalue como verdadera.

'''

hamburguesas = 0    ### Esta es mi variable que sirve como parte de la condicion.
                    ### Basicamente si es True se ejecuta, si se vuelve False se detiene el bucle y continua con la siguiente instruccion

while hamburguesas < 20:        ## Mientras que mi variable sea menor 
    print("Me chingo otra!")    ## Imprime un string
    hamburguesas+=1             ## Sumamos uno a la variable cada que pasa por el bucle hasta que se complete


### DO-WHILE ### 

'''
Esta es una estructura de control que repite un bloque de codigo al menos una vez, y luego verifica una condicion parea decidir si continuar o salir del bucle

La cual no existe dentro de python.
'''
### BREAK ### 

'''
El break dentro de un bucle WHILE, detiene el bucle si la condicion es verdadera

'''

i = 1

while i < 6:    ### Mientras i sea menor que 6
    print(i)    ### Imprime i
    if i == 3:  ### Si i es igual a 3
        break   ### Detenemos el bucle
    i += 1      ### Sumamos una a i cada bucle

### Continue ###

'''
El CONTINUE detiene una de las iteraciones o condiciones, y pasa al lo siguente dentro del loop, de manera que termine la condicion inicial.

Dentro de este condicional, lo que nos plantea es como detener dentro de un punto y continuar al siguiente.

'''

i = 0

while i < 10:   ### Mientras i sea menor que 10   
    i+=1        ### Suma uno a i
    if i == 3:  ### Si i es igual a 3, lo omite dentro del ciclo y continua
        continue 
    print(i)     ### Imprime i


while i < 10:
    i+=1
    print(i)

### FOR ### 

'''
Esta es una estructura de control que permite repetir un bloque de codigo un numero especifico de veces.

Dentro de los lenguajes, un bucle for consta de tres partes initialization, update, condition

for(initialization; condition; update)
{
	// hacer algo
}

Aqui lo que nos esta diciendo es, que requiere una variable o un argumento inicial, despues requiere una condicion para el bucle, y finaliza la construccion con un adaptador


Dentro de python no tiene bucle FOR como tal. Únicamente tiene WHILE y FOR EACH, que actúa sobre colecciones iterables. Para emular conseguir el resultado de un FOR hay que emplear una de estas estructuras, por ejemplo así:


### FOREACH ###


El bucle FOREACH es una estructura de control que se basa en realizar acciones por elementos dentro del bucle, el cual se repite hasta que se hayan terminado todos los elementos dentro del bucle.

Por otro lado, Python el bucle FOREACH se realiza con la palabra reservada for. De hecho, Python no dispone de un bucle FOR como tal, siempre es un bucle FOREACH.
'''

for i in range(1, 101): ### Damos una condicion dentro del bucle
    print(i)            ### Donde imprmimos i dentro del rango de i hasta 100

coleccion = [1, 2, 3, 4, 5] ### Tenemos una lisa con elementos

for elemento in coleccion: ### Por cada elemento dentro de la lista coleccion
    print(elemento)        ### Imprimimos un elemento


"""
Podemos hacer bucles dentro de bucles, esto nos permite realizar acciones mas complejas.

Si tengo que realizar ese calculo para todas las aula y todos los alumnos de cada una de ellas, un bucle anidado es la solución más sencilla.

Sin embargo, la anidación de bucles también tiene sus problemas. La principal de ellas es que la cantidad de bucles que se ejecutamos aumenta exponencialmente.

Si, por ejemplo, tienes un bucle que se ejecuta 10.000 veces, dentro de un bucle que se ejecuta 10.000 veces, ¡el bucle interno se va a ejecutar 100 millones de veces!

"""
rows = 3 ### Tenemos tres filas
cols = 3 ### Tenemos tres columnas

for m in range(rows):       ### Para m dentro del range de 3 filas, vamos a imprimir m
    for j in range(cols):   ### Pero antes necesitamos recorrer el bucle de j para las columnas
        print(m,j)          ### Una vez los bucles terminen se pueden repetir

"""
Lo que estamos haciendo dentro del siguiente bucle es pasar por la primer vuelta de m, pero antes de terminar es primer vuelta, tenemos que hacer el bucle de j hasta que termine, una vez terminado este bucle podemos continuar con la siguiente vuelta de m, y asi sucesivamente hasta terminar con el bucle inicial
"""