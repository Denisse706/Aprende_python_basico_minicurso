import re

text= "Este es un ejemplo de una página web: https://www.youtube.com/watch?v=QVwCG9v1mqI y tambien podemos visitar"

pattern = "https?://[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)