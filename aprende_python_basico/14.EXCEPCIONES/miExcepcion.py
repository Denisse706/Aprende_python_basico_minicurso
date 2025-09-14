#CREANDO MI PROPIA EXCEPCION PERSONALIZADA
class MiExcepcion(Exception):
    def _init_(self, err):
        print(f"cometiste el siguiente error: {err}")

try: #MANEJANDO MI PROPIA EXCEPCION 
    #raise lanza exxcepciones
    raise MiExcepcion ("esto es el raise una excepcion")
except:
    print("esta es la excepcion")