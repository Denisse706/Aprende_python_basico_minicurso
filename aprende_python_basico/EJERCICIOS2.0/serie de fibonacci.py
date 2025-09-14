# CREANDO UNA FUNCION QUE MUESTRE LA SERIE FIBONACCI ENTRE EL 0  EL NUMERO DADO
#PRIMERO CREAMOS LA FUNCION, UNA TUPLA QUE LUEGO VAMOS A DESEMPAQUETAR

def fibonacci(num):
    a,b = 0,1   # Inicializamos los dos primeros números de la serie
    fibonacci_list = [] # Lista vacía para almacenar la serie
    for i in range(num): # Iteramos hasta `num` veces
        if b > num: return fibonacci_list
        else: 
            fibonacci_list.append(a) # Agregamos el número a la lista
            a,b = b, a+b  # (a) representa el nummero de vueltas del rango para llegar al numero final (b) 
    return fibonacci_list

resultado = fibonacci(8) #a = 5 iteraciones y b = [0,1,1,2,3,5,8]
print(resultado)

#1️⃣ Primera vuelta:
#a = 1, b = 0 + 1 = 1

#2️⃣ Segunda vuelta:
#a = 1, b = 1 + 1 = 2

#3️⃣ Tercera vuelta:
#a = 2, b = 1 + 2 = 3

#4️⃣ Cuarta vuelta:
#a = 3, b = 2 + 3 = 5

#5️⃣ Quinta vuelta:
#a = 5, b = 3 + 5 = 8

