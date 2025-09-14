import pandas as pd
import matplotlib.pyplot as plt #LIBRERIA PARA VISUALIZAR DATOS DE FORMA GRAFICA
import seaborn as sns #LIBRERIA DE GRAFICOS ESTADISTICOS

df = pd.read_csv("13.ARCHIVOS\\problemas_graficos\\3dispersion.csv", encoding= "UTF-8")



#CREANDO GRAFICO DE DISPERSION SNS Y scatterplot
sns.scatterplot(x="tiempo",y="dinero",data=df)



#MOSTRAR EL GRAFICO
plt.show()
