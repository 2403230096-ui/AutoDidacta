'''
Nombre: Marco Adel Lopez Angulo
Fecha: 17/11/2026

El dia de hoy voy a documentarme respecto al punto de programacion conocido como los condicionales y operadores logicos.

Tipos, Ideas, Usos, Ejemplos.

Todo se busca que este englobado dentro de este archivo para poder comprender, los aspectos de la programacion que todavia son incognitas para el usuario


'''

"""
Principalmente las condicionales son operaciones o estructuras que permiten al programa tomar una decision, en base a condiciones.

"""
### IF ###
'''
Esta es una condicion que ejecuta un bloque de codigo si dicha condicion es verdadera.

Y se aplica cuando las condiciones son un True o False.
Basicamente Funciona con operacones booleanas las cuales dependeiendo del resultado pensado, pueden dar paso a realizar una o varias acciones dentro de un bloque de codigo.

'''

mi_nombre = "Marco Adel Lopez Angulo"
var = True

if var == True:
    print(mi_nombre)

### Si la condición es true, el programa sigue, ejecutando el código
### Si la condición es false, el programa salta, y no ejecuta el cuerpo del código


X = input("Que numero es X? \n")
Y = input("Que numero es Y \n")


### Lo que buscamos aqui es que la condicional nos de un resultado de True or False
### De esta manera sabemos si el tema en cuestion esta bien estructurado

if X > Y:
    print(f"{X} es mas grande que {Y}\n")


### En caso de que haya mas de una accionque pueda suceder dentro del arbol de decisiones
### Se puede dar pociones diferentes con el uso de IF-ELSE

### IF-ELSE ###
'''
Esto al igual que el if nos permite ejecutar un bloque de codigo, pero dentro del IF-ELSE este nos permite ejecutar dentro del booleano False

Basicamente hablando de si algo no para (true), entonces realiza lo siguiente (false).

'''

if X > Y: ## X es mayor que Y, entonces imprime el primer print
    print(f"{X} es mas grande que {Y}") 
elif X < Y: ### X es menor que Y, entonces Y es mas grande que X e imprime el segundo print nadamas
    print(f"{Y} es mas grande que {X}")
else: ### En este caso son iguales, por lo que solo puede imprimir el ultimo print
    print(f"{Y} no es mas grande que {X}")

### ELSE ###

'''
Esto es basicamente en caso de que todas la condicionales principales no se cumplen, muestra un resultado definitivo. 

En caso para las condicionales, en programas mas desarrollados este se usa como una verificacion, un bloque de codigo que en el caso de que las condicionales fallen por algun parametro, este pueda reiniciar la condicional o dar una advertencia respecto al fallo o carencia dentro del bloque de codigo.
'''

if X > Y: ## X es mayor que Y, entonces imprime el primer print
    print(f"{X} es mas grande que {Y}") 
elif X < Y: ### X es menor que Y, entonces Y es mas grande que X e imprime el segundo print nadamas
    print(f"{Y} es mas grande que {X}")
else: ### En este caso son iguales, por lo que solo puede imprimir el ultimo print
    print(f"{Y} no es mas grande que {X}")


### SWITCH ###

'''
Es un condicional que nos permite ejecutar ciertos bloques de codigo dependeiendo de el valor de la expresion o variable.

Es una estructura alternativa para la condicional IF-ELSE, ya que dentro de este condicional el programa no tiene que pasar por todas las lineas de codigo, ya que el valor funciona como un apuntador hacia el bloque de codigo que se debe de utilizar

Dentro de los casos, se finaliza con un break, para asi evitar la ejecucion de Switch u otros bloques de codigo.

El ultimo caso o default, se ejecuta cuando la expresion no coincide con ninguno de los casos definidos dentro del switch.

'''

DiaSemana = int(input("Escoge el dia de la semana (1-7)?\n"))

match DiaSemana:
    case 1: 
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No coincide con ningun dia")

### OPERADORES LOGICOS ###

'''
Estos operadores son utilizados para realizar operaciones booleanas en valores y variables. De esta manera se hace uso de la combinacion de cndiciones para llegar a un resultado final.

Los operadores Logicos serian AND, OR, y NOT

AND = True AND True = True ## Si ambas son true se puede avanzar
OR = True OR False = True ## Si una de ellas es True se puede Avanzar
NOT = NOT True = False ## Si no es true, no se avanza


'''


HrsEstudio = int(input("Que rango de horas estudiaste?\n 1) 1-2 hrs\n 2) 3-4 hrs\n 3) 5-6 hrs\n 4) 7-8 hrs\n"))
HrEspecifica = int(input("Cuantas horas especificas?\n"))


match HrsEstudio:
    case 1:
        if HrEspecifica == 1:
            print("Vuelve a Estudiar")
        elif HrEspecifica > 1 and HrEspecifica <= 2:
            print("Estudios Regulares")
        else:
            print("Registra un numero de horas")
    case 2:
        if HrEspecifica == 3:
            print("Estudio Sobresaliente")
        elif HrEspecifica > 3 and HrEspecifica <= 4:
            print("Estudios Excelente")
        else:
            print("Registra un numero de horas")
    case 3:
        if HrEspecifica == 5:
            print("Estudio Prolongado")
        elif HrEspecifica > 5 and HrEspecifica <= 6:
            print("Maraton de Estudios")
        else:
            print("Registra un numero de horas")
    case 4:
        if HrEspecifica == 7:
            print("Horas Preocupantes")
        elif HrEspecifica > 7 and HrEspecifica <= 8:
            print("Exceso de Estudios")
        else:
            print("Registra un numero de horas")
    case _:
        print("Rango Excesivo o nulo de horas")