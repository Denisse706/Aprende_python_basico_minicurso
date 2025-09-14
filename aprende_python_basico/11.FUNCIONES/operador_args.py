
#UTILIZANDO EL OPERADOR ARGS (*)
def suma_total(numeros):
    return sum([*numeros])
resultado = suma_total ([5,4,6,8,8,4,2,4])
print(resultado)

#LO MISMO PERO UTILIZANDO EL OPERADOR ARGS COMO PARAMETRO
def suma(nombre, *nummero):
    return f"{nombre}, la suma de tus numeros es: {sum(nummero)}"

resultado = suma("Lian",5,12,5,3,6)
print(resultado)

