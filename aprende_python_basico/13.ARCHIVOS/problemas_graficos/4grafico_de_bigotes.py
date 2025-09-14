import pandas as pd
import matplotlib.pyplot as plt #LIBRERIA PARA VISUALIZAR DATOS DE FORMA GRAFICA
import seaborn as sns #LIBRERIA DE GRAFICOS ESTADISTICOS

df = pd.read_csv("13.ARCHIVOS\\problemas_graficos\\4bigotes.csv", encoding= "UTF-8")



#CREANDO GRAFICO DE bigotes SNS Y boxplot
sns.boxplot(x="categoria",y="valor",data=df)



#MOSTRAR EL GRAFICO
plt.show()
