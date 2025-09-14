#AND
RESULTADO  = True & True #Devolver true 
RESULTADO2 = True & False #Devolver false
RESULTADO3 = False & True #Devolver false
RESULTADO4 = False & False #Devolver false

#OR
RESULTADO5 = True | True #Devolver true 
RESULTADO6 = True | False #Devolver true
RESULTADO7 = False | True #Devolver true
RESULTADO8 = False | False #Devolver false

#NOT
RESULTADO9 = not True #Devolver false
RESULTADO10 = not False #Devolver true

#AEUSENCIA DE VALOR
RESULTADO11 = None

#EJEMPLO

# Pedimos al usuario que ingrese sus datos
usuario = input("Ingrese su usuario: ")  
password = input("Ingrese su contraseña: ")  

# Definimos qué usuarios están registrados
usuarios_validos = ["user1", "user2", "admin"]

# Verificamos si el usuario está registrado
usuario_registrado = usuario in usuarios_validos  

# Verificamos si la contraseña es correcta (suponemos que la correcta es "1234")
password_correcto = (password == "1234")  

# Evaluamos la condición de acceso
if (usuario_registrado and password_correcto) or (usuario == "admin"):
    print("✅ Acceso permitido")  
else:  
    print("❌ Acceso denegado")  