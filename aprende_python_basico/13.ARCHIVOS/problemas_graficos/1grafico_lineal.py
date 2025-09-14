import pandas as pd
import matplotlib.pyplot as plt #LIBRERIA PARA VISUALIZAR DATOS DE FORMA GRAFICA
import seaborn as sns #LIBRERIA DE GRAFICOS ESTADISTICOS

df = pd.read_csv("13.ARCHIVOS\\problemas_graficos\\1vasos_agua.csv", encoding= "UTF-8")

#CREANDO GRAFICO DE LINEAS CON SNS Y lineplot
sns.lineplot(x="fecha",y="vasos",data=df)

#MARCANDO UNA INTERSECCION
plt.plot("01-14",10,"o") #FECHA, NUMERO DE VASOS Y UN "O" PARA INDICAR LA MARCACION

#MOSTRAR EL GRAFICO
plt.show()
