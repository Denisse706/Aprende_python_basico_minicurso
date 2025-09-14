#CUANDO USAR CONJUNTOS ✅ set → Si necesitas evitar duplicados y no te importa el orden.
#CUANDO USAR TUPLAS ✅ tuple → Si necesitas una colección ordenada pero inmutable (por seguridad o eficiencia).
#LOS CONJUNTOS Y LAS TUPLAS NO SON MODIFICABLES COMO LAS LISTAS Y CADENAS
#PARA VERIFICAR QUE FUNCIONES O METODOS TIENEN EN EL DICCIONARIO 

tupla = (tuple(("ESTAS", "SON", "TUPLAS")))
print(tupla)
print(dir(tuple("kffffrkr"))) #TUPLA

conjunto = (set(["ESTOS", "SON", "CONJUNTOS"]))
print(conjunto)
print(dir(set (["jsdffsflks", "jsflkfjslfs"])))

#SORTED ORDENA UNA LISTA DE ORDEN ASCENDENTE A DESCENDENTE Y SE PUEDE USAR CON TUPLA, DIC ETC
orden = sorted(tupla)
print(orden)

#SORTED ORDENA UNA LISTA DE ORDEN ASCENDENTE A DESCENDENTE Y SE PUEDE USAR CON TUPLA, DIC ETC
orden = sorted(conjunto)
print(orden)