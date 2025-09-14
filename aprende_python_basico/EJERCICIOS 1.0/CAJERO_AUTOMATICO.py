#Practica bucles while con condiciones de salida.
#Usa condicionales (if-elif-else) para manejar distintas opciones.
#Aplica entrada del usuario (input()) y conversión de datos (float()).
#Permite entender operaciones matemáticas básicas con variables.

#SIMULADOR DE CAJERO AUTOMATICO
#El usuario podrá:
#✅ Consultar saldo
#✅ Depositar dinero
#✅ Retirar dinero
#✅ Salir del sistema


saldo = 1000 #saldo inicial

while True:
    print("\n💰 Cajero Automático 💰")
    print("\n1. Consultar saldo")
    print("\n2. Depositar dinero")
    print("\n3. Retirar dinero")
    print("\n4. Salir")
    opcion = input ("elige una opcion del 1-4: ")

    if opcion == "1":
        print(f"\n🔹 Tu saldo actual es: $ {saldo}")
    elif opcion == "2":
        cantidad = float(input("\n💲 Ingrese la cantidad a depositar:"))
        if cantidad > 0:
            saldo+=cantidad 
            print(f"✅ Depósito exitoso. Nuevo saldo: ${saldo}")
        else:
            print("❌ Error: Ingresa una cantidad válida.")
    elif opcion =="3":
        cantidad= float (input("\n💲 Ingrese la cantidad a retirar: "))
        if 0 < cantidad <= saldo:
            saldo -= cantidad
            print(f"✅ Retiro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("❌ Error: Fondos insuficientes o cantidad no válida.")
    elif opcion == "4":
        print("\n👋 ¡Gracias por usar el cajero! Hasta luego.")
        break
    else:
        print("❌ Opción inválida. Inténtalo de nuevo.")
