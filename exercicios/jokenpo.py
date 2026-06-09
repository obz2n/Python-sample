import random
import time

# ============================
# Variáveis globais
# ============================
pontuação_jogador = 0
pontuação_computador = 0
rodada_atual = 0
máximo_rodadas = 3


# ============================
# Funções
# ============================
def escolha_jogador():
    while True:
        escolha = input("\nEscolha (pedra/papel/tesoura): ").lower()
        if escolha in ["pedra", "papel", "tesoura"]:
            return escolha
        print("Opção inválida! Digite: pedra, papel ou tesoura")


def escolha_computador():
    escolhas = ["pedra", "papel", "tesoura"]
    return random.choice(escolhas)


def determinar_vencedor(jogador, computador):
    global pontuação_jogador, pontuação_computador

    if jogador == computador:
        return "Empate!"

    combinações_vitória = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}

    if combinações_vitória[jogador] == computador:
        pontuação_jogador += 1
        return "Você venceu!"
    else:
        pontuação_computador += 1
        return "Computador venceu!"


def exibir_resultado(jogador, computador, resultado):
    print(f"\nVocê escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")
    print(f"Resultado: {resultado}")
    print(f"Placar - Você: {pontuação_jogador} | Computador: {pontuação_computador}")


def jogar_rodada():
    global rodada_atual
    rodada_atual += 1

    print(f"\n{'=' * 40}")
    print(f"Rodada {rodada_atual}")
    print(f"{'=' * 40}")

    escolha_player = escolha_jogador()
    escolha_computer = escolha_computador()
    resultado_rodada = determinar_vencedor(escolha_player, escolha_computer)
    exibir_resultado(escolha_player, escolha_computer, resultado_rodada)


def mostrar_resultado_final():
    print(f"\n{'=' * 40}")
    print("FIM DO JOGO!")
    print(f"{'=' * 40}")
    print("Placar Final:")
    print(f"Você: {pontuação_jogador}")
    print(f"Computador: {pontuação_computador}")

    if pontuação_jogador > pontuação_computador:
        print("\n Você é o campeão! ")
    elif pontuação_computador > pontuação_jogador:
        print("\n O computador é o campeão! ")
    else:
        print("\n Jogo terminou em empate! ")


def principal():
    print(f"{'=' * 40}")
    print("Bem-vindo ao JOKENPO!")
    print(f"{'=' * 40}")
    print(f"Melhor de {máximo_rodadas} rodadas\n")

    while rodada_atual < máximo_rodadas:
        jogar_rodada()
        time.sleep(1)

    mostrar_resultado_final()


# ============================
# Execução do jogo
# # ============================
if __name__ == "__main__":
    principal()
