# Pedimos al usuario un número entero
n = int(input("Ingrese un número: "))

# 1. Tabla de multiplicar de n desde 1 hasta 12
print(f"\nTabla de multiplicar del {n}:")
for i in range(1, 13):  # Iteramos desde 1 hasta 12
    print(f"{n} x {i} = {n * i}")

# 2. Primeras 10 potencias de n
print(f"\nPrimeras 10 potencias de {n}:")
for i in range(1, 11):  # Iteramos de 1 a 10
    print(f"{n}^{i} = {n ** i}")

# 3. Pirámide de números
print(f"\nPirámide de números hasta {n}:")
for i in range(1, n + 1):  # Iteramos desde 1 hasta n
    for j in range(1, i + 1):  # Imprimimos números en cada fila
        print(j, end=" ")  # Mostramos los números en la misma línea
    print()  # Nueva línea después de cada fila

# 4. Cuadrado de asteriscos
print(f"\nCuadrado de tamaño {n}:")
for i in range(n):
    print("* " * n)

# 5. Verificar si n es un número perfecto
def es_numero_perfecto(num):
    suma_divisores = sum(i for i in range(1, num) if num % i == 0)
    return suma_divisores == num

if es_numero_perfecto(n):
    print(f"\n{n} es un número perfecto.")
else:
    print(f"\n{n} no es un número perfecto.")

# 6. Menú interactivo
while True:
    print("\nMenú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion in ["1", "2", "3", "4"]:
        if opcion == "4":
            break
    else:
        print("Opción inválida, intente nuevamente.")

# 7. Verificación de contraseña
contraseña_correcta = "secreta"
while True:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == contraseña_correcta:
        print("Contraseña correcta.")
        break
    print("Contraseña incorrecta, intente nuevamente.")

# 8. Cálculo de raíz cuadrada por aproximaciones sucesivas
def raiz_cuadrada_aproximada(num, tolerancia=0.0001):
    aproximacion = num / 2.0
    while abs(aproximacion ** 2 - num) > tolerancia:
        aproximacion = (aproximacion + num / aproximacion) / 2.0
    return aproximacion

print(f"\nRaíz cuadrada aproximada de {n}: {raiz_cuadrada_aproximada(n)}")

# 9. Verificación de número de teléfono
while True:
    telefono = input("Ingrese un número de teléfono (10 dígitos): ")
    if telefono.isdigit() and len(telefono) == 10:
        print("Número de teléfono válido.")
        break
    print("Número inválido, intente nuevamente.")

# 10. Cálculo de la sumatoria sum(x-1)^(a-1)
n = int(input("Ingrese el valor de n: "))
a = int(input("Ingrese el valor de a: "))
resultado = sum((x - 1) ** (a - 1) for x in range(1, n + 1))
print(f"\nEl resultado de la sumatoria es: {resultado}")
