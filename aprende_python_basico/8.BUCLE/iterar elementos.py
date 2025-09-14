#FUNCIONNA PARA LISTAS, TUPLAS  Y CONJUNTOS

#creando una lista para iterar
animales = ["perro", "gato","glondrina","grillo","lobo"]
#recorriendo lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")

#creando una tupla para iterar
numeros = (35,26,33,48,59)
#recorriendo la lista numeros
for numero in numeros:
    resultado = numero * 7
    print(f"estos son los numero por 7: {resultado}")

#iterando dos listas al mismmo tiempo
for numero, animal in zip (numeros, animales):
    print (f"esta es la lista 1: {numero}")
    print(f"esta es la lista 2: {animal}")

#FORMAS DE RECORRER UNA LISTA

#USANDO ENUMERATE 
for num in enumerate(numeros):
    #print(num)  #nos devuelve tuplas, el indice del elemento y el valor del mismo
    #print(num[0]) #para acceder al indice se coloca [0]
    #print(num[1]) #para acceder al valor del elemento [1]
    #PARA ACCEDER A LOS DOS SE COLOCA
    indice = num[0]
    valor = num [1]
    print(f"el indice es: {indice} y el valor es {valor}")

#USANDO ELSE
for numero in numeros:
    print(f"ejecutando el bucle valor atual:{numero}")
else:
    print("el bucle terminó")


