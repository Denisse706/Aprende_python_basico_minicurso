import re

Text = "Reemplazando todas las vocales por el asterisco"

new_text = re.sub("[aeiou]", "*",Text)

print(new_text)

