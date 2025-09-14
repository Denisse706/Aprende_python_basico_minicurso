#CREANDO UNA FUNNCION QUE DEVUELVA NUMEROS PRIMOS HASTA LLEGAS AL NUMERO QUE LE ENTREGAMOS INICIALMENTE

#CREANDO LA FUNCION QUE DETERMINE SI UN NUMERO ES PRIMO
def es_primo(num):
    #verificamos que el numero pasado no pueda 
    # dividirse por ningun numero entre 2 y ese mismo nummero +1
    for i in range(2, num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i== 0: return False
        #si termina termina el bucle significa que no fue divisible entonce es true
    return True

#CREANDO FUNCION QUE RETORNE UN LISTA CON TODOS LOS NUMEROS PRIMOS 
def primos_hasta(num):
    #creamos una lista
    primos = []
    for i in range(2, num +1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    #devolvemos la lista de numeros primos
    return primos
#creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(27)
print(resultado)

#FORMA CORTA DE LLEGAR AL MISMO RESULTADO
primos_hasta = lambda num: list(filter(lambda a: all (a % b != 0 for b in range (2, int (a ** 0.5)+1)), range (2, num)))
print(primos_hasta(27))