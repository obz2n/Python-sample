'''
Desafio
Encontrar o maior e menor numero inputados pelo usuário

Problema
Serão 3 inputs para saber qual o menor valor e o maior valor
'''

def encontrar_maior_menor(valores):
    """
    Recebe uma lista de valores e imprime o maior e o menor.
    """
    if not valores:
        print("Nenhum valor fornecido.")
        return
    
    maior = max(valores)
    menor = min(valores)
    print(f'O maior valor digitado é: {maior}')
    print(f'O menor valor digitado é: {menor}')

# Execução do programa
if __name__ == "__main__":
    # lista de valores
    valores = []
    for i in range(1, 4):
        valor = int(input(f'{i}º valor: '))
        valores.append(valor)
    encontrar_maior_menor(valores)