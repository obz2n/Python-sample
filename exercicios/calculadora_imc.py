"""
Calculadora de IMC
"""

nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura**2)


def descobrir_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        return "Peso normal"
    elif imc >= 25.0 and imc <= 29.9:
        return "Sobrepeso"
    elif imc >= 30.0 and imc <= 34.9:
        return "Obesidade grau I"
    elif imc >= 35.0 and imc <= 39.9:
        return "Obesidade grau II"
    elif imc > 40:
        return "Obesidade grau III"


tipo_imc = descobrir_imc(imc)

print("=" * 60)
print(f"Olá {nome}, o seu IMC é {imc:.2f}")
print(f"\n O seu tipo é: {tipo_imc}")
print("=" * 60)
