import pandas as pd

df = pd.read_csv("13.ARCHIVOS\\txt_csv\\problemas_resueltos\\p_texto.csv", encoding= "UTF-8")

#CAMBIAR EL TIPO DE DATO DE UNA COLUMNA

#CONVERTIR A STRING LOS DATOS DE UNA COLUMNA
#df ["edad"] = df ["edad"].astype (int)
#print (type(df["edad"][2]))        #MOSTRAR LOS DATOS DEL ELEMENTO SOLICITADO EN LA COLUMNA DADA

#REMPLAZANDO EL NOMBRE DE UNA COLUMNA POR OTRO
df ["apellido"].replace("marquez","tutankamon", inplace= True)
#print(df["apellido"])

#ELIMINANDO LAS FILAS SIN DATOS
df = df.dropna()
#print(df)

#CONVIRTIENDO LAS EDADES A ENTEROS
df ["edad"] = df ["edad"].astype (int)

#ELIMINANDO FILAS REPETIDAS
df = df.drop_duplicates()
print(df)

#CREANDO EL ARCHIVO LIMPIIO YA MODIFICADO
df.to_csv("13.ARCHIVOS\\txt_csv\\problemas_resueltos\\texto_limpio.csv")


