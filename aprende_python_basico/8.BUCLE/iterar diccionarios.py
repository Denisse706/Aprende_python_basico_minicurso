diccionario = dict (nombre = "amancio", apellido = "ortega", edad = "80")


#CON KEY VEMOS LA CLAVE PERO NO EL VALOR
for key in diccionario:
    print(key)

#PARA ITERAR EL ELEMENTO ES DECIR RECORRERLO VIENDO SU CLAVE Y SU VALOR CORRESPONDIENTE
for key in diccionario.items():
    print(key) #ESTO NOS DEVUELVE UNA TUPLA CLAVE : VALOR

#PARA ENTENDERLO MEJOR SERIA
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} Y el valor es: {value}") #AQUI SE IMPRIME EN 1 LINEA
    #print(f"la clave es: {key}") #SE PUEDE DECIR EN DOS LINEAS
    #print(f" el valor es: {value}")
   