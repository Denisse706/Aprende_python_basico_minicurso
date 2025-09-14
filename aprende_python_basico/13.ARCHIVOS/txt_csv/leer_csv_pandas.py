#PARA ESTO HAY QUE INSTALAR PIP
import pandas as pd
#USANDO FUNCION READ_CSV PARA LEER EL ARCHIVO CSV
df = pd.read_csv("13.ARCHIVOS\\txt_csv\\texto.csv", encoding= "UTF-8" )  
df2 = pd.read_csv("13.ARCHIVOS\\txt_csv\\texto.csv", encoding= "UTF-8" )  
#El archivo es como una hoja de calculo con datos por eso lo llamamos data frame o df 

# Limpieza de nombres de columnas
df.columns = df.columns.str.strip().str.replace('"', '').str.lower()

#ORDENANDOLO DE FORMA DESCENDIENTE O ASCENDENTE
df1= df.sort_values('edad', ascending=True)
df2 = df.sort_values('edad', ascending=False)
#CONCATENANDO LOS DOS DATAFRAMES
df_concatenado = pd.concat([df1, df2])
#print(df_concatenado)

#ACCEDIENDO A LA PRIMERA FILA CON head()
firt_row = df.head(3)

#ACCEDIENDO A LA ULTIMA FILA CON TAIL()
last_row = df.tail(3)

#ACCEDIENDO A LAS COLUMNAS Y FILAS CON SHAPE 
filas_totales, columnas_totales = df.shape

#OBTENIENDO LA DATA ESTADISTICA DEL DF (USO EN IA)
df_info = df.describe()

#ACCEDIENDO A UN ELEMENTO ESPECIFICO DEL DF CON LOT
elemento_especifico_loc = df.loc[2, "edad"] #(fila, columna)

#ACCEDIENDO A UN ELEMENTO ESPECIFICO DEL DF CON ILOT
elemento_especifico_iloc = df.iloc[2, 2] #(fila, columna)

#ACCEDIENDO A TODAS LAS FILAS DE UNA COLUMNA CON ILOT
apellidos = df.iloc[:,1] #(fila, columna)

#ACCEDIENDO A FILAS EN DONDE LA EDAD SEA MAYOR A 30
edad_mayor_30 = df.loc[df["edad"]>30,:]

print(edad_mayor_30)




#SLAICING: muestra el punto de partida y el ultimo numero que se quiere leer con (numero inicial : numero final)
#cadena = "0123456789"
#print(cadena[3:9]) #firts number : last number
#print(cadena[:]) # all numbers
#print (cadena[:3]) #all numbers up to 3
#print (cadena[3:]) #all numbers starting from 3
