import re

# La cadena en la que se buscarán los patrones 
text = "La fecha es 23/06/2021 y el telefono es +1-555-555-5555"

# El patrón a buscar
pattern = r"\d{2}/\d{2}/\d{4}" #[{2 veces un numero y /} {2 veces un numero y /} {4 veces un numero}]

# El texto con el que se reemplazará el patrón 
replacement = "Fecha oculta"

# Remplazar todas las apariciones del patrón en la cadena de texto
new_tex = re.sub(pattern, replacement, text)

# Imprimir el resultado
print("Texto modificado:", new_tex)