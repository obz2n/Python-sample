produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: R$ "))
quantidade = 0

def estoque():
    opcao = int(input("Escolha uma opção:\n1 - Adicionar estoque\n2 - Remover estoque\n3 - Verificar estoque\n"))
    if opcao == 1:
        adicionar = int(input("Digite a quantidade a ser adicionada: "))
        quantidade_atualizada = quantidade + adicionar
        print(f"Estoque atualizado. Novo estoque de {produto}: {quantidade_atualizada} unidades.")
    elif opcao == 2:
        remover = int(input("Digite a quantidade a ser removida: "))
        if remover > quantidade:
            print("Quantidade insuficiente em estoque.")
        else:
            quantidade_atualizada = quantidade - remover
            print(f"Estoque atualizado. Novo estoque de {produto}: {quantidade_atualizada} unidades.")
    while opcao != 0:
        opcao = int(input("Escolha uma opção:\n1 - Adicionar estoque\n2 - Remover estoque\n3 - Verificar estoque\n0 - Sair\n"))
        if opcao == 1:
            adicionar = int(input("Digite a quantidade a ser adicionada: "))
            quantidade_atualizada = quantidade + adicionar
            print(f"Estoque atualizado. Novo estoque de {produto}: {quantidade_atualizada} unidades.")
        elif opcao == 2:
            remover = int(input("Digite a quantidade a ser removida: "))
            if remover > quantidade:
                print("Quantidade insuficiente em estoque.")
            else:
                quantidade_atualizada = quantidade - remover
                print(f"Estoque atualizado. Novo estoque de {produto}: {quantidade_atualizada} unidades.")
        elif opcao == 3:
            print(f"O estoque atual de {produto} é: {quantidade_atualizada} unidades.")
        elif opcao == 0:
            print("Saindo do programa.")
        else:
            print("Opção inválida.")
estoque()
