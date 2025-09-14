#creando conjunto con set
conjunto = set (["dato1", "dato2", "dato3"])
#no se pueden crear diccionarios vacios sin la funcion set

#agregando un conjunto dentro de otro conjunto
conjunto1 = frozenset (["dato1","dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#TEORIA DE CONJUNTOS
conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {2, 4, 6}

#PARA VERIFICAR SI UN CONJUNTO ES UN SUBCONJUNTOO DE OTRO
resultado = conjunto2.issubset(conjunto1) #issubset determina si un conjunto es subconjunto de otro
resultado = conjunto2 <= conjunto1 #USANDO <= TAMBIEN SE PUEDE COMPROBAR SI UN CONJUNTO ES SUBCONJUNTO DE OTRO

#PARA VERIFICAR SI UN CONJUNTO ES UN SUPERCONJUNTO DE OTRO
resultado = conjunto1.issuperset (conjunto2) #issuperset determina si un conjunto es un superconjunto de otro
resultado = conjunto1 > conjunto2 # > determina lo mismmo de otra forma

#PARA VERIFICAR SI HA UN NUMERO EN COMUN

resultado = conjunto1.isdisjoint(conjunto2) #ISDISJOINT verifica si ha numeros en comun entre conjuntos
#va a ser true solo cuando los conjuntos que se comparan no tienen datos en comun
print(resultado) #EN ESTE CAJO IMPRIME FALSE PORQUE HAY NUMEROS EN COMUN

