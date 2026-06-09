# contagem utilizando for
for i in range(1, 11):
    print(i)


# contagem utilizando while
contagem = 0
while contagem < 10:
    contagem = contagem + 1
    print(contagem)


# Verificar se um numero é par ou impar utilizando if e else
num = int(input("Digite um numero: "))

if num % 2 == 0:
    print("O seu numero é par")
else:
    print("O seu numero é ímpar")


# Soma de numeros pares
n = int(input("Digite um nunmero: "))
soma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        soma = soma + i
print(f"A soma dos numeros pares de 1 a {n} é: {soma}")

# Soma de numeros pares utilizando while
n = int(input("Digite um numero: "))
soma = 0
contador = 1
while contador <= n:
    if contador % 2 == 0:
        soma = soma + contador
    contador = contador + 1
print(f"A soma dos numeros pares de 1 a {n} é: {soma}")

# Fatorial de um numero utilizando for
num = int(input("Digite um numero: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial = fatorial * i
print(f"O fatorial de {num} é: {fatorial}")
