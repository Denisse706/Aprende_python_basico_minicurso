#CREANDO FUNCION DE 3 PARAMETROS
def frase(nombre, adjetivo, apellido): 
    return f"hola {nombre} {apellido}, eres una {adjetivo}"

#UTILIZANDO KEWORDS ARGUMENTS
frase_resultado = frase(adjetivo = "genia", nombre = "luz", apellido = "lopez")
print(frase_resultado)

#CREANDO LA MISMA FUNCION CON UN PARAMETRO OPCIONAL  UN VALOR POR DEFECTO
def frase(nombre, apellido, adjetivo = "INTELIGENTE"):
    return f"hola {nombre} {apellido} eres super {adjetivo}"
frase_resultado = frase("glenda", "gray")
print(frase_resultado) 

#CREANDO UNA NUEVA FUNCION CON FILTER (FUNCION BULD_IN)

numero = [1,2,3,8,4,5,6,22]
#CON FILTER FILTRAMOS CUAL DE LOS NUMERO DE LA LISTA ES PAR

def es_par(num):
    if (num%2==0):
        return True
numeros_pares = filter(es_par, numero)
print(list(numeros_pares))