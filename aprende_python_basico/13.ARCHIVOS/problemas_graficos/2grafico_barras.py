import pandas as pd
import matplotlib.pyplot as plt #LIBRERIA PARA VISUALIZAR DATOS DE FORMA GRAFICA
import seaborn as sns #LIBRERIA DE GRAFICOS ESTADISTICOS

df = pd.read_csv("13.ARCHIVOS\\problemas_graficos\\2cofla_ingresos.csv", encoding= "UTF-8")



#CREANDO GRAFICO DE BARRAS CON SNS Y barplot
sns.barplot(x="fuente",y="ingresos",data=df)

#MOSTRANDO EL TOTAL DE INGRESOS
total_ingresos = df['ingresos'].sum()
print(f"El total de ingresos es de: {total_ingresos} USD")

#MOSTRAR EL GRAFICO
plt.show()
