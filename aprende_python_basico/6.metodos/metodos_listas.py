#CUANDO USAR LIST: ✅ list → Si necesitas una colección ordenada y modificable.

print(dir(list))

#CREANDO LISTA CON LIST
list1= list (["marcos", "juana", "colon", 45, True])
list2= list ([90, 10, False, 45, True])
list3 = list (["k", "x", "a","b","z"])


#LEN DEVUELVE LA CANTIDAD DE ELEMENTOS QUE HA EN LA LISTA
cantidad_elementos = len(list1)
print(cantidad_elementos)

#APPEND AGREGA UN ELEMENTO A LA LISTA 
list1.append("nuevo1")
print(list1)

#INSERT AGREGA UN ELEMENTO A LA LISTA EN LA POSICION QUE ELIJA 
#PRIMERO VA LA POSICION Y LUEGO EL ELEMENTO NUEVO A AGREGAR
list1.insert( 2,"NUEVO2")
print(list1)

#EXTEND AGREGA UNA LISTA A UNA LISTA COMO PARAMETROS INDIVIDUALES A LA LISTA YA EXISTENTE
list1.extend([2020,False])
print(list1)

#POP ELIMINA UN ELEMENTO DE UNA LISTA, PIDE INDICE Y DEVUELVE VALOR
list1.pop(1) 
list1.pop(-1)#PARA ELIMINAR EL ULTIMO SE COLOCA -1 O SI SE QUIERE ELIMINAR EL ANTE ULTIMO -2 ASI SUCESIVAMENTE
print(list1)

#REMOVE REMUEVE ELEMENTO DE UNA LISTA, PIDE NOMBRE DEL ELEMENTO
list1.remove("nuevo1")
print(list1)

#CLEAR ELIMINA TODOS LOS ELEMENTOS DE UNA LISTA
#list.clear()

#SORT ORDENA UNA LISTA DE ORDEN ASCENDENTE A DESCENDENTE, MODIFICA LA LISTA. ESTA FUNCION SOLO PUEDE SER USADA EN LISTAS
list2.sort()
print(list2)

#SORTED TIENE LA MISMA FUNCION DE SORT Y SE PUEDE USAR CON TUPLA, DIC ETC. NO MODIFICA LA LISTA O TULPA ETC ORIGINAL
orden = sorted(list3, reverse=True) #EL REVERSE TRUE SE USA PARA ORDENAR EN REVERSA
print(orden)


#REVERSE INVIERTE LOS ELEMENTOS DE UNA LISTA, EL ELEMENTO 1 PASA A SER EL ULTIMO Y VICEVERSA
list2.reverse()
print(list2)

#INDEX VERIFICA SI SE ENCUENTRA UN ELEMENTO EN LA LISTA
elemento_encontrado = list1.index("marcos") #deberia devolver 0 que es la posicion en la que se encuentra "marcos"
print(elemento_encontrado)
