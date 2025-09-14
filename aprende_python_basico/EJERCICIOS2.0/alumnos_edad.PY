#HO FALTO EL PROFESOR DE CLASES Y LOS ALUMNOS SE ORGANIZARON PARA ARMAR LA SUYA
# 1 ALUMNO SERA EL PROFESOR (EL DE MAYOR EDAD)
# 1 ALUMNNO SERA EL ASITENTE (EL DE MENOR EDAD)
# A) PERDIR EL NOMBRE  Y LA EDAD DE LOS ALUMNOS Y ORDENAR LOS DATOS DE MAYOR A MENOR
# B) DETERMINAR CUAL DEBE SER EL PROFESOR Y CUAL EL ASISTENTE 

def obtener_alumnos(cantidad_alumnos):
   
    alumnos = []
    for i in range (cantidad_alumnos): 
        nombre = input("ingresa tu nombre: ")
        edad = int(input("ingresa tu edad: "))
        alumno = (nombre, edad) #LA VARIABLE ALUMNO ES UNA TUPLA CON EL NOMBRE Y LA EDAD
        alumnos.append(alumno)
    alumnos.sort(key=lambda x: x[1])

    asistente = alumnos[0][0]
    profesor = alumnos [-1][0]
    return asistente, profesor
asistente, profesor = obtener_alumnos(5) #SUPONIENDO QUE VINIERO 5 ALUMNOS SE EJECUTARA EL BUCLE 5 VECES
print(f"el profesor es {profesor}, el asistente es {asistente}")