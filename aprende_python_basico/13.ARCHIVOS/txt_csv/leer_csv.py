import csv

with open("13.ARCHIVOS\\txt_csv\\texto.csv", encoding="utf-8") as archivo:
    #print(archivo.read()) SE EJECUTA

    reader = csv.reader(archivo)
    #para recorrerlo
    for row in reader: #esto va a recorer fila por fila
        print(row)

    
