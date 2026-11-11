'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

 bucle de "for" en rango para imprimir dentro del bucle del 1 al 100
	Si "i" (numero dentro del bucle) es modular a 3 y su resultado es igual a 0 y Si "i" (numero dentro del bucle) es 	modular a 3 y su resultado es igual a 0
		Entonces escribe en consola "fizzbuzz"
	Si "i" (numero dentro del bucle) es modular a 3 y su resultado es igual a 0
		Entonces escribe en consola "fizz"
	Si "i" (numero dentro del bucle) es modular a 5 y su resultado es igual a 0
		Entonces escribe en consola "buzz"
	En cualquier otro caso de i:
		Imprime el numero
        
 '''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0 :
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else: 
        print(i)
