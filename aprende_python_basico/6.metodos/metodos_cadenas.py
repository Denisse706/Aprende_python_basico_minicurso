cadena1 = "hola"
cadena2 = "bien y tu? bien amigo. mucha suerte"
cadena3 = "151354"
cadena4 = "ffddrrgrrrgrs"

# para ver las propirdades de cada tipo de dato en los metodos en cadena se les agrega la funcion dir 
#colocamos
#print(dir(tipo de dato))
#probaremos ahora con datos del tipo string
#para probar las propiedades colocamos

print (dir("string"))

#METODO PARA CONVERTIR UN VALOR

#upper convierte a mayusculas
mayus = cadena1.upper() 
print(mayus)

#lower convierte a minusculas
minus = cadena1.lower() 
print(minus)

#capitalize convierte la primera letra a mayuscula 
primer_letra_mayuscula = cadena2.capitalize()
print(primer_letra_mayuscula)


#METODOS PARA ENCONTRAR UN VALOR

#con find buscamos una cadena en otra cadena, si no hay coincidencias develve -1
busqueda_find= cadena2.find("?")
print(busqueda_find) 

#con index  buscamos una cadena en otra cadena, si no hay coincidencia devuelve un exepción
busqueda_index= cadena2.index("?")
print(busqueda_index)

#METODOS PARA CONTAR

#count cuenta las coincidencias de una cadena en otra cadena, si no hay coincidencias develve 
contar_coincidencias = cadena2.count("e")
print(contar_coincidencias)

#METODOS PARA CONSULTAR UN VALOR
#consulta si un texto es numerico, devuelve true y si no es devolvemos false
es_numeric = cadena3.isnumeric()
print(es_numeric)

#consulta si un texto es alphabetico, devuelve true y si no es devolvemos false
#sin contar espacios es decir una oracion o frase sin espacios o devuelve false
es_alfabetico = cadena4.isalpha()
print(es_alfabetico)

#METODOS PARA VERIFICAR

#Startswith verifica si una cadena empieza con una cadena dada si es si devuelve true
empieza_con = cadena2.startswith("bi")
print(empieza_con)

#Endswith verifica si una cadena termine con una cadena dada si es si devuelve true
termina_con = cadena2.endswith("erte")
print(termina_con)

#Replace remplaza un valor por otro
remplaza_valor = cadena2.replace("bien", "genial")
print(remplaza_valor)

#Split crea una lista a partir de una cadena y el lugar que se elija
#en este ejemplo le pido que convierta a lista las palabras que se encuentran entre las palabras "bien"
cadena_separada = cadena2.split ("bien")
print(cadena_separada)
#FUNCIONES

#Len cuenta cuantos caracteres tiene una cadena contando sus espacios
contar_caracteres = len(cadena2)
print(contar_caracteres)