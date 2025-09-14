#CREANDO DICCIONARIO CON DICT
diccionario = dict (nombre = "amancio", apellido = "ortega")
#no se pueden crear diccionarios vacios sin dict

#las listas no pueden ser claves porque son iterables
diccionario = {("margaret", "amancio"): "nombre"}
#usamos frozenset para introducir conjuntos en un dict
diccionario = {frozenset(["margaret", "amancio"]): "nombre"}

#CREANDO DICCIONARIOS CON fromkeys() valores none o sin asignar
diccionario = dict.fromkeys(["nombre","apellido"])
print(diccionario)

#CON KEY VEMOS LA CLAVE PERO NO EL VALOR

for key in diccionario:
    print(key)
