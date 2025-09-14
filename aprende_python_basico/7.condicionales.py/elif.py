salario = 20000
gasto_mensual = 11000
ingreso_mensual = salario - gasto_mensual


if salario > 15000:
    print("estas bien en cualquier parte del mundo")
    if ingreso_mensual > 10000:
       print("bien sigue así")
    elif ingreso_mensual >= 0:
        print("se te esta llendo de la mano los gastos")
    elif ingreso_mensual < 0:
        print ("estas en quiebra")
    
elif salario > 3000:
     print("estas bien en cualquier parte de latinoamerica")

elif salario > 800:
     print ("trata de ahorrar, porque eres esclavo de tu empleo")

else:
     print("haz mas plata que no te alcanza ni para ahorrar")