import re 
text = "The quick brown fox jumps over the lazy dog"

x = re.search("^The.*dog$",text) #Buscar [inicio de texto, busqueda con coincidencias, final de texto]

if x:
    print("SI")
else:
    print("NO")
    