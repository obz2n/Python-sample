# _*_ coding: utf-8 _*_

# programa para calcular o valor de compra minima
# de tintas para um determinado metro quadrado e valor 
# minimo de compra

a = int(input("Escreva os metros quadrados: "))
while a < 100:
    print("Valor de compra minimo = 100 metros quadrados")
    a = int(input("Digite novamente os metros quadrados: "))

litro = a / 3
preco_lata = 80
litro_lata = 18
latas = int(litro / litro_lata)
total = int(latas * preco_lata)
print("total de latas a serem usadas:",latas)
print("valor total a pagar:", total)
print("Fim do Programa")


