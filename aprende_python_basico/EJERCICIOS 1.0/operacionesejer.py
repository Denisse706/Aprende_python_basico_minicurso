 #Obtener el resto y el cociente de las siguientes divisiones enteras:
#(a) 45 entre 3 (b) 111 entre 67
#(c) 99 entre 54 (d) 103964 entre 7

#para obtener el resto se emplea %  para obtener el cociente se emplea //

a_resto = 45 % 3
a_cociente = 45 // 3
print(f"el resto de 45 entre 3 es: {a_resto} y el cociente del mismo es: {a_cociente}")

b_resto = 111 % 67
b_cociente = 111 // 67
print(f"el resto de 111 entre 67 es: {b_resto} y el cociente del mismo es: {b_cociente}")

c_resto = 99 % 54
c_cociente = 99 // 54
print(f"el resto de 99 entre 54 es: {c_resto} y el cociente del mismo es: {c_cociente}")

d_resto = 103964 % 7
d_cociente = 103964 // 7
print(f"el resto de 103964 entre 7 es: {d_resto} y el cociente del mismo es: {d_cociente}")


#PARA HACER ESTE PROCESO EN UNA SOLA LINEA A LA VEZ CON UNA FUNCIÓN SE USA: DIVMOD
#DIVMOD ES UN TIPO DE DATO <CLASS 'TUPLE'>
#ESTE REFLEJA EL COCIENTE COMO CLASE  y EL RESTO COMO TUPLA (COCIENTE, RESTO)
cocienrest =  divmod(103964, 7)
print(cocienrest) 
