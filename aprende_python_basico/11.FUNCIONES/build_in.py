#LAS FUNCIONES buid_in SON FUNCIONES INTEGRADAS POR PYTHON
#ADEMAS DE LAS A VISTAS EXISTE OTRAS IGUAL DE IMPORTANTE

numeros = [1,22,5,67,9,88]

#PARA ENCONTRAR EL NUMERO MAYOR DE UNA LISTA
numero_mayor = max(numeros)
print(numero_mayor) #88

#PARA ENCONTRAR EL NUMERO MENOR DE UNA LISTA
nummero_menor = min(numeros)
print(nummero_menor) #1

#DIVMOD ES UN TIPO DE DATO <CLASS 'TUPLE'>
#ESTE REFLEJA EL COCIENTE COMO CLASE  y EL RESTO COMO TUPLA (COCIENTE, RESTO)
cocienrest =  divmod(103964, 7)
print(cocienrest) 

#ROUND PARA REDONDEAR (lo que coloque luego de la "," es el numero de decimale a los que quiero redondear)
numero = round(13.1233533,4)
print(numero)

#BOOL RETORNA FALSE SI ES LISTA VACIO/NONE O ES == 0  SI ES STRING O !=0  RETORNA TRUE
resultado = bool (132153)
print(resultado)

#ALL RETORNA TRUE SI TODOS LOS VALORES SON VERDADEROS  EN UNA LISTA
resultado_all = all([1,25,"KDFJLF"])
print(resultado_all)

#SUM SUMA TODOS LOS ELEMENTOS DE UNA LISTA 
num1 = [1,5,6]
num2 = [2,55,7]
num3 = [88,56]
suma_num1 = sum(num1 + num2)
print(suma_num1)

#SUMA DE TODAS LAS LISTAS
suma_all_list = sum(num1+num2+num3)
print(suma_all_list)

#POW ES == X**Y O X ELEVADO A Y
valor = 2
elevacion = pow(2,5) #EL 2 SE MULTIPLICA POR SI MMISMO 5 VECES
print(elevacion)

#OTRAS FUNCIONES ARITMETICAS SON 
#abs (x) . Proporciona el valor absoluto de x.


