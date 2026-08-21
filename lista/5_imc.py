def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
# Programa principal
peso = 86
altura = 1.81
imc = calcular_imc(peso, altura)

print("IMC:", imc)

if imc < 18:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")  