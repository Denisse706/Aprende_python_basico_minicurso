import re #EL MODULO (re) ES USADO PARA TRABAJAR CON EXPRESIONES REGULARES

texto = '''Hola ben, ¿cómo estas? esta es la cadena 1.
Bien bin 256 ¿y tu?, 2 cadena
última cadena'''

#BUSQUEDAS SIMPLES

resultado1 = re.search("bien",texto) #SEARCH ENCUENTRA COINCIDENCIAS Y LAS DEVUELVE
#print(resultado1)

resultado2 = re.findall("cAdeNa",texto, flags= re.IGNORECASE) #ENCUENTRA TODAS LAS COINCIDENCIAS Y LAS DEVUELVE
#SE LE AGREGA EL PARAMETRO FLAGS = IGNORECASE EL CUAL IGNORA MAYUSCULAS O MINUSCULAS
#print(resultado2)

#EXPRESIONES REGULARES:

#\d --- busca digitos numericos del 0 al 9
resultado3= re.findall(f"\d",texto)
#print(resultado3)

#\D --- busca TODO MENOS digitos numericos
resultado4= re.findall(f"\D", texto)
#print(resultado4)

#\w --- busca caracteres alfanumericos [A-Z, a-z, 0-9, _]
resultado5 = re.findall(f"\w",texto)
#print(resultado5)

#\W --- busca TODO MENOS caracteres alfanumericos [espacios, saltos de linea (\n), signos de puntuacion(,?!)]
resultado6= re.findall(f"\W", texto)
#print(resultado6)

#\s --- busca espacios en blanco [espacios, saltos de linea, tabs]
resultado7 = re.findall(f"\s",texto)
#print(resultado7)

#\S --- busca TODO MENOS espacios en blanco
resultado8= re.findall(f"\S", texto)
#print(resultado8)

#. --- busca TODO MENOS saltos de linea
resultado9= re.findall(f".", texto)
#print(resultado9)

#\n --- busca saltos en linea
resultado10= re.findall(f"\n",texto)
#print(resultado10)

#\ --- cancela caracteres especiales
resultado11= re.findall(f"\.",texto) #cancelando la funcion (.) para buscar (".") dentro del texto
#print(resultado11)

#ARMANDO UNA CADENA QUE BUSQUE SEGUIDO: ["UN NUMERO","UN PUNTO","UN ESPACIO"] 
resultado12 = re.findall(f'\d\.\n', texto) #DEBE TENER ESE ORDEN SI NO LO CUMPLE NO LO MUESTRA
#print(resultado12)

#^ --- Saber si una determinada palabra es la que inicia el texto
resultado13= re.findall(f"^Hola",texto, flags= re.M) #el parametro M indica que la busqueda debe ser multilinea
#cada linea con el parametro M se interpreta como un nueva, ahora se puede buscar las palabras que inician las otras lineas
#print(resultado13)

#$ --- Saber si una determinada palabra es la que finaliza el texto
resultado14= re.findall(f"cadena$",texto, flags= re.M)
#print(resultado14)

#{n} --- Busca n cantidad de veces el valor de la izquierda
resultado15= re.findall(r'\d{3}',texto)
#rint(resultado15)

#{n,m} --- Busca n cantidad y máximo m cantidad de veces
resultado16 = re.findall(r'\d{1,3}',texto) #1 coincidencia como maximo 3 o más
resultado16 = re.findall(r'na{1,2}',texto) # busca las letras "na" en donde se encuentre 1 o 2 veces
#print(resultado16)

# | --- Encuentra alguno de los dos datos que se piden o encuentra ambos
resultado17= re.findall(r'\d{1,2}|Hola',texto)
print(resultado17)

# * --- Encuentra cero o mas ccoincidencia
resultado18= re.findall(r'n*',texto)
print(resultado18)