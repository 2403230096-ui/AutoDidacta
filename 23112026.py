"""
Nombre: Marco Adel Lopez Angulo
Fecha: 23/11/2026

Día 6: pseudocódigo, diagramas de flujo y descomposición de problemas - palíndromos, contar vocales y números primos.
Día 7: repaso, mini-evaluación y cierre de los 15 ejercicios sin ayuda.


- N: longitud de la palabra.
- N - 1: último índice válido.
- i: índice actual.
- Índice inverso: posición correspondiente desde el final.
Consolidación del aprendizaje
La expresión que debes intentar construir es:

Índice inverso = (N-1)-i

"""

### Palindromo ###

def buscar_palindromo(): ### funcion para definir palindromo
    texto = input("Ingresa la palabra que vas a utilizar:\n") ### Ingresamos el texto / caracteres
    palabra = texto.lower() ### Convertimos el texto en minusculas
    longitud = len(palabra) ### Numero de letras en la palabra
    mitadpalabra = longitud // 2 ### Verificamos que la mitad de la palabra para usarlo en el       recorrido de la funcion
    for i in range(mitadpalabra):
        if palabra[i] != palabra[longitud - 1 - i]:
            return False
    else:
        return True


resultado = buscar_palindromo()

if resultado == True:
    print("La palabra es un palindromo")
else:
    print("La palabra no es palindromo")


### Contar Vocales ###

def contar_vocales():
    vocales = ("a","i","u","e","o","á","é","í","ó","ú")
    texto = input("Ingresa el texto:\n")
    texto_ingresado = texto.lower()
    conteo_vocales = 0
    for i in texto_ingresado:
        if i in vocales:
            conteo_vocales += 1

    return conteo_vocales

datos_conseguidos = contar_vocales()
print(datos_conseguidos)    

### Numero Primo ### 

def num_primo():
    ultimo_num = int(input("Ingresa un numero: \n"))
    for i in range(0, ultimo_num + 1):
        print(i)

numero = num_primo()
print(numero)