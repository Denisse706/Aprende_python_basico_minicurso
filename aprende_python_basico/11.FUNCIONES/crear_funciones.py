#PARA CREAR UNA FUNCION SIMPLE
#def saludar():
   #print ("Hola brou")
#para que la funcion se repita muchas veces 
#saludar()
#saludar()

#CREAR UNA FUNCIONN QUE TENGA PARAMETROS


def saludar (nombre, sexo): 
  
  sexo = sexo.lower()
  if (sexo == "mujer"):
       pronombre = "a Capitana"
  elif (sexo == "hombre"):
       pronombre = "o Capitan"
  else:
        pronombre = "o Marinero"
  
  print(f"Bienvenido al Barco {nombre}, ahora seras nuestr{pronombre}")
saludar("camila","mujer")
saludar("andres", "marino")

#CREAR UNA FUNCION QUE ME RETONER VALORES
def crear_contraseña_aleatorea(num):
     chars = "erpdfvbslhjgm"
     numero_entero = str(num)
     num = int(numero_entero[0])
     c1 = num -2
     c2 = num 
     c3 = num -5
     contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
     return contraseña #con return se guarda el valor retornado 

password = crear_contraseña_aleatorea(5)
frase = f"tu contraseña nueva es {password}"
print(frase)
