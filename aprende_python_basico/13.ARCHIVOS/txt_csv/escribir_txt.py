#PARA EDITAR EL TEXTO REESCRIBIENDO Y SUPLANTANDO POR EL TEXTO EXISTENTE
#SE USA "W" WRITE
with open('13.ARCHIVOS\\txt_csv\\texto.txt', 'w', encoding="utf-8") as archivo:
    #WRITE REESCRIBE EL TEXTO EXISTENTE
    archivo.write("este texto esta reescrito")
    #print(archivo)
    #WRITELINE ESCRIBE UNA LINEA EXTRA A LA YA EXISTENTE
    archivo.writelines([" linea writelines, random"])
    archivo.writelines(["\n""salto de linea" "\n" "otro salto de linea"])
    archivo.write(", linea write")
    print(archivo)

#PARA AÑADIR UNA LINEA VARIAS VECES SE UNA "a" APPEND
with open ("13.ARCHIVOS\\texto.txt", 'a', encoding="utf-8") as archi:
    #AÑADIENDO EL ARCHIVO
    for i in range (5):
        archi.write("\n""Esto se repite")
        archi.write(f" (linea {i+1})")
