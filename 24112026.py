def num_primo():
    ultimo_num = int(input("Ingresa un numero: \n"))    ### Numero al cual va a llegar nuestro rango 
    if ultimo_num <= 0:
        return False
    for i in range(1, ultimo_num + 1):                  ### Bucle que recorre el rango de numeros indicados desde 1
        divisores = 0                                   ### Contador para divisores
        if i < 1:                                       ### Si i es mayor que 1 continuamos
            pass
        elif divisores > 2:                             ### Si los divisores son mayores a dos, este no es un numero primo
            print(f"{i}, no es un numero primo")
        elif i % i == 0 and i % 1 == 0:                 ### Si i entre i da un residuo de 0 es una division exacta y Si i entre 1 da un residuo de 0 es una division exacta
            for j in range(i + 1, i):                          ### Por cada iteracion de i, hacemos un blucle para encontrar posibles divisores
                if i % j == 0:                           ### Si el numero de la iteracion divido entre i == 0, lo agregamos a divisores
                    divisores += 1 




