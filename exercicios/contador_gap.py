# contador de gap baseado no conteudo do youtuber de extremo sucesso.

gap = 0
print("=" * 60)
print(f"Quanto de gap ja tomei ate o momento: {gap}")
while True:
    try:
        gap += int(input("Acrescentar gap: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro: ")
print("=" * 60)
print(f"Gap atual: {gap}")
print('Opções: "s" para continuar, "n" para sair, "r" para resetar.')
print("Deseja continuar? (s/n/r)")
opcao = input()
while opcao != "s" and opcao != "n" and opcao != "r":
    print(
        "Opção inválida. Digite 's' para continuar ou 'n' para sair ou 'r' para resetar."
    )
    opcao = input()
if opcao == "s":
    while True:
        try:
            gap += int(input("Acrescentar gap: "))
            print(f"gap atual: {gap}")
            print("Deseja continuar? (s/n/r)")
            opcao = input()
            while opcao != "s" and opcao != "n" and opcao != "r":
                print(
                    "Opção inválida. Digite 's' para continuar ou 'n' para sair ou 'r' para resetar."
                )
                opcao = input()
            if opcao == "n":
                print(f"Gap final: {gap}")
                print("Encerrando o programa.")
                break
            elif opcao == "r":
                gap = 0
                print("Gap resetado para 0.")
                break
            continue
        except ValueError:
            print("Entrada inválida. Digite um número inteiro: ")
elif opcao == "n":
    print(f"Gap final: {gap}")
    print("Encerrando o programa.")
elif opcao == "r":
    gap = 0
    print("Gap resetado para 0.")
print("=" * 60)
