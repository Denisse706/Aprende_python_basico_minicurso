calcular_imc = lambda p, a: p / a**2

peso, altura = map(float, (input("Peso (kg): "), input("Altura (m): ")))

imc = calcular_imc(peso, altura)

match imc:
    case _ if imc < 18.5: categoria = "Bajo peso"
    case _ if imc < 24.9: categoria = "Peso normal"
    case _ if imc < 29.9: categoria = "Sobrepeso"
    case _: categoria = "Obesidad"

print(f"IMC: {imc:.2f} - {categoria}")