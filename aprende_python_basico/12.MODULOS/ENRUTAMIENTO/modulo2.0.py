#SI EL MODULO ESTUVIERA EN UNA CARPETA EN LA MISMA RUTA SE IMPORTA ASI:
#import funciones_saludos.Saludar as saludos

#PERO SI ESTUVIERA UNA CARPETA AFUERA SE IMPORTA CON SYS:
import sys
sys.path.append("C:\\Users\\Usuario\\Desktop\\DDD\\curso python\\12.MODULOS\\funciones_saludos")
import Saludar

print(Saludar.saludo_ingles("frank"))