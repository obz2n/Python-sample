from time import sleep

print("=" * 15)
print("MERCADINHO")
print("=" * 15)
compra = float(input("Preço das Compras: "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista no cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
pagamento = int(input("Escolha a forma de pagamento: "))
while pagamento > 4 or pagamento < 1:
    pagamento = int(
        input("Forma de pagamento não encotrada. Por favor digite novamente: ")
    )
if pagamento == 1:
    print(
        f"Sua compra de R${compra:.2f} vai custar R${compra - (compra * 15 / 100):.2f} à vista"
    )
elif pagamento == 2:
    print(
        f"Sua compra de R${compra:.2f} vai custar R${compra - (compra * 10 / 100):.2f} à vista no cartão"
    )
elif pagamento == 3:
    print(
        f"Sua compra de R${compra} vai custar 2x de R${compra + (compra * 5 / 100):.2f} no cartão"
    )
elif pagamento == 4:
    quantidade = int(input("Selecione a quantidade de vezes para parcelar: "))
    print(
        f"A sua compra de R${compra} vai custar R${compra + (compra * 8 / 100):.2f} em {quantidade}x no cartão"
    )
escolha = int(input("Para finalizar compra digite 1. Para Cancelar compra digite 2: "))
while escolha != 1 and escolha != 2:
    escolha = int(input("Escolha não econtrada. Por favor, digite novamente: "))
if escolha == 1:
    print("Finalizando a sua compra")
    sleep(3)
    print("Processando pagamento...")
    sleep(2)
    print("Pagamento realizado com sucesso. Obrigado e volte sempre!")
elif escolha == 2:
    print("Compra cancelada!")
