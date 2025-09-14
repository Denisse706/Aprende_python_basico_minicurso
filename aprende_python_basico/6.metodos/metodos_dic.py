#CUANDO USAR DICT 🏆 dict → Si necesitas asociar claves con valores para acceso rápido.
# ✅ Cuando necesitas asociar claves con valores y acceder a ellos de forma rápida.
#✅ Cuando quieres evitar claves duplicadas, pero mantener valores únicos.
#✅ Cuando necesitas una estructura flexible y modificable.

diccionario = {
    "nombre": "marcos",
    "apellido": "polo",
    "edad": 69,
    "año de nacimiento": 1254
}

#KEYS () → DEVUELVE LAS CLAVES (tambien sirve para iterar)
#nos devuelve un elemento de tipo dict_items
claves=diccionario.keys()
print(claves)

#SORTED ORDENA UNA LISTA DE ORDEN ASCENDENTE A DESCENDENTE Y SE PUEDE USAR CON TUPLA, DIC ETC
orden = sorted(diccionario)
print(orden)

#GET () → DEVUELVE EL VALOR DE UNA CLAVE (si no encuentra nada el programa continua)
valor_elemento = diccionario.get ("nombre")
print(valor_elemento)

#CLEAR () → ELIMINA TODOS LOS ELEMENTOS DEL DICCIONARIO
#diccionario.clear()

#POP () → ELIMINA UN ELEMENTO 
diccionario.pop("edad")
print(diccionario)

#ITEMS () → PARA ITERAR UN DICT (obtener un elemento dict_items iterable)
diccionario_iterable = diccionario.items()
print(diccionario_iterable) #sin embargo aunque aparezca un resultado este no es iterable ya que no se puede recorrer los elementos