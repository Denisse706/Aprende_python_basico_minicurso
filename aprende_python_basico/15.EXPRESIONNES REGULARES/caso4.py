import re

email = "example@example.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
    print("direccion de correo valida")
else:
    print("direccion de correo invalida")
    