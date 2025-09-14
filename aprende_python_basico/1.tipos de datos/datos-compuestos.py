
#creando listas (se pueden modificar y van con [])
list = ["andres", 35, True]

#para modificar una lista
list [0] = "cerecita"

#creando tupla (no se puede modificar y van con ())
tuple =("mirta", 65, False)

#tanto las tuplas como los conjuntos no se pueden modificar, pero si redefinir todos los datos 
#los conjuntos son un tipo de dato desordenado que no se puede duplicar y solo se puede acceder a el mediante un bucle

#creacndo conjuntos
conjunto = {"lila", 80, True}
#print (conjunto[0]) → no se puede acceder

#creando diccionario (dict)
dict = {
    "nombre": "koala",
    "edad" : 36,
    "altura" : 1.90
}
#la estructura del diccionario es key : value (clave: valor) y se accede al dato por medio de su key o clave

#para ejecutar (lista, tupla y diccionario )

print (list[0])
#cerecita
print (tuple [2])
#false
print (dict["edad"] + 3)
#36 + 3 = 39

