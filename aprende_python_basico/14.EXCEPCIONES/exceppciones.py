#CREANDO FUNCION QUE SUME 2 NUMEROS
def sum_dos():

    while True: #INICIANDO UN BUCLE
        
        a= input("numero 1:  ") #SOLICITANTO VALOR
        b= input("numero 2:  ") #SOLICITANTO VALOR
        
        try: #INTENTAR REALIZAR LA SUMA 
            resultado = int(a) + int(b) #ESPECIFICAR QUE DEBEN SER ENTEROS

        except: #EN CASO DE QUE NO SE INGRESEN NUMEROS ENTEROS LANZAR UNA EXCEPCION
            print("inténtalo nuevamente") #PEDIRLE QUE REINGRESE LOS DATOS
        else: #ADEMAS SI SE EJECUTA CORRECTAMENTE 
            break #TERMINAR EL BUCLE

        finally: #EL FINALLY SE EJECUTA SIEMPRE
            print("esto se ejecuta siempre")

    return resultado #MOSTRANDO RESULTADO

print(sum_dos())
