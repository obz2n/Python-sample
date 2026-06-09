# _*_ coding:utf-8 _*_

# Programa para verificar o calculo dos lados de um triangulo
# e verificar se e um triangulo RETANGULO, OBTUSANGULO, ACUTANGULO
# EQUILATERO ou ISOSCELES

A = float(input("Primeiro Valor: "))
B = float(input("Segundo Valor: "))
C = float(input("Terceiro Valor: "))

x = 0

if A < B:
    x = A
    A = B 
    B = x
    
if B < A:
    x = B
    B = A
    A = x
    
if C < B:
    x = C
    C = B 
    C = x

if (A > B+C):
    print("NAO FORMA TRIANGULO")
elif (A**2 == B**2 + C**2):
    print("TRIANGULO RETANGULO")
elif (A**2 > B**2 + C**2):
    print("TRIANGULO OBTUSANGULO")
elif (A**2 < B**2 + C**2):
    print("TRIANGULO ACUTANGULO")
elif (A==B and A==C):
    print("TRIANGULO EQUILATERO")
elif ((A==B and A!=C) or (B==C and B!=A)):
    print("TRIANGULO ISOSCELES")
print("Fim do Programa")
