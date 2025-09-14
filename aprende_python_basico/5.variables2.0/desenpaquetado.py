# desempaquetamiento en Python es el proceso 
# de extraer los elementos de una colección, como una lista, tupla o diccionario, 
# y asignarlos a variables. EL DESEMPAQUETAMIENTO NO FUNCIONA EN CONJUNTOS

#EJEMPLO
#no se pueden crear diccionarios vacios sin la funcion tuple
tupla = tuple (["libro", "mesa"])


datos_tupla = "libro","mesa" #tanto en tupla como en lista los elementos los toma en el orde en que se escriben
datos_lista = ["libro","mesa"]#elemento 1 = libro es decir objeto = libro, elemento 2 = mesa, lugar = mesa


objeto, lugar = datos_tupla

print(tupla) #sera igual a mesa