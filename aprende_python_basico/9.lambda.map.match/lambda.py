#Una función lambda en Python es una función anónima que 
# se define en una sola línea. Se usa para crear funciones 
# pequeñas sin necesidad de usar def.

#Sintaxis básica de lambda
#lambda argumentos: expresión

#argumentos → Los parámetros de la función (puede haber múltiples, separados por comas).

#expresión → Lo que se evalúa y devuelve (no necesita return).

#Ejemplo 2: Múltiples parámetros

#CON DEF SE NECESITAN VARIAS LINEAS DE CODIGO PARA OBTENER UN RESULTADO ASÍ
def numerito(a, b):
    return a + b
print(numerito(3, 7))

#CON LAMBDA EN DOS LINEAS DE CODIGO SE OBTIENE EL MISMO RESULTADO
suma = lambda a, b: a + b
print(suma(3, 7))  # Salida: 10
#Aquí a y b son los argumentos, y la expresión a + b es lo que devuelve.


# Ejemplo 3: lambda dentro de map() y filter()
# Usando map()
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Salida: [2, 4, 6, 8, 10]
# map() aplica la función lambda a cada elemento de la lista.



# Usando filter()
numeros = [10, 25, 30, 5, 50]
mayores_20 = list(filter(lambda x: x > 20, numeros))
print(mayores_20)  # Salida: [25, 30, 50]
# filter() usa lambda para quedarse solo con los valores que cumplen la condició


# Ejemplo 4: lambda dentro de sorted()
personas = [("Ana", 25), ("Luis", 20), ("Carlos", 30)]
ordenado = sorted(personas, key=lambda x: x[1])  # Ordenar por edad
print(ordenado)  # Salida: [('Luis', 20), ('Ana', 25), ('Carlos', 30)]
#  Aquí lambda extrae el segundo valor (edad) de cada tupla para ordenarlas.

#¿Cuándo usar lambda?
#✅ Para funciones cortas que no se reusarán mucho.
#✅ En map(), filter(), sorted() y estructuras similares.
#❌ No usar cuando la función es compleja (usar def en su lugar). 

#MAS EJEMPLOS
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Salida: [2, 4, 6, 8, 10]
#lambda x: x % 2 == 0 → Retorna True solo si el número es par.
#filter() aplica la función lambda a cada número de la lista y solo deja los True.
#list() convierte el resultado en una lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impar = list(filter(lambda x: x % 2 == 1, numeros))
print(impar)
#lambda x: x % 2 == 1 → Retorna True solo si el número es par.

nombres = ["Ana", "Bernardo", "Carlos", "David", "Elena"]
ordenados = sorted(nombres, key=lambda nombre: len(nombre))

print(ordenados)  
# Salida: ['Ana', 'Elena', 'David', 'Carlos', 'Bernardo']

#PARA HACER UNA FUNCION LAMBDA QUE RETORNE VALORES PARES
numeros = [1,5,9,8,3,26,4,2]
numeros_pares = filter(lambda numero: numero%2 ==0, numeros )
print(list(numeros_pares))