frutas = ["mandarina","melocoton","melon","mora","kiwi","maracuyá"]

#PARA SACAR UN ELEMENTO EL CUAL NO QUEREMOS QUE SE CUENTE
#AGREGAR CONTINUE
for fruta in frutas:
    if fruta == "kiwi":
        continue
    # print(fruta)


#PARA EVITAR QUE EL BUCLE SE SIGA EJECUTANDO
#AGREGAR BREAK
for fruta in frutas:
    if fruta == "mora": #este condicional puede ir escrito luego del print(fruta) 
        #de esta forma el bucle finaliza luego de que aparezca el elemento
        break
    print(fruta) #estando print luego de la condicional el bucle finaliza antes de que aparezca el elemento
print("bucle finalizado")

#recorrer cadena de texto
cadena="color"
for letra in cadena:
    print(letra)

#FOR EN UNA SOLA LINEA DE CODIGO
numeros = [1,22,6,5,7]

numero_duplicado = [x*2 for x in numeros]
print(numero_duplicado)