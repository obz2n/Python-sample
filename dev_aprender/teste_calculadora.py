# ============================================================
#  Calculadora Interativa
# ============================================================

import math


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
    return a / b


def potencia(a, b):
    return a**b


def raiz_quadrada(a):
    if a < 0:
        raise ValueError(
            "Erro: Não é possível calcular a raiz quadrada de um número negativo."
        )
    return math.sqrt(a)


def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
    return a % b


def exibir_menu():
    print("\n" + "=" * 40)
    print("        🧮  CALCULADORA PYTHON")
    print("=" * 40)
    print("  [1]  Adição              ( + )")
    print("  [2]  Subtração           ( - )")
    print("  [3]  Multiplicação       ( × )")
    print("  [4]  Divisão             ( ÷ )")
    print("  [5]  Potenciação         ( ^ )")
    print("  [6]  Raiz Quadrada       ( √ )")
    print("  [7]  Módulo / Resto      ( % )")
    print("  [0]  Sair")
    print("=" * 40)


def obter_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️  Entrada inválida. Digite um número válido.")


def formatar_resultado(valor):
    # Exibe sem casas decimais se for inteiro
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.6f}".rstrip("0")


def executar_operacao(opcao):
    operacoes_dois_operandos = {"1", "2", "3", "4", "5", "7"}

    if opcao in operacoes_dois_operandos:
        a = obter_numero("  Digite o primeiro número : ")
        b = obter_numero("  Digite o segundo número  : ")

        if opcao == "1":
            resultado = somar(a, b)
            operador = "+"
        elif opcao == "2":
            resultado = subtrair(a, b)
            operador = "-"
        elif opcao == "3":
            resultado = multiplicar(a, b)
            operador = "×"
        elif opcao == "4":
            resultado = dividir(a, b)
            operador = "÷"
        elif opcao == "5":
            resultado = potencia(a, b)
            operador = "^"
        elif opcao == "7":
            resultado = modulo(a, b)
            operador = "%"

        print(
            f"\n  ✅  {formatar_resultado(a)} {operador} {formatar_resultado(b)} = {formatar_resultado(resultado)}"
        )

    elif opcao == "6":
        a = obter_numero("  Digite o número          : ")
        resultado = raiz_quadrada(a)
        print(f"\n  ✅  √{formatar_resultado(a)} = {formatar_resultado(resultado)}")


def main():
    historico = []

    print("\n  Bem-vindo à Calculadora Python!")
    print("  Digite o número da operação desejada.")

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "0":
            if historico:
                print("\n" + "=" * 40)
                print("  📋  Histórico de operações:")
                for i, entrada in enumerate(historico, 1):
                    print(f"  {i:>2}. {entrada}")
            print("\n  👋  Encerrando a calculadora. Até logo!\n")
            break
        elif opcao in {"1", "2", "3", "4", "5", "6", "7"}:
            try:
                # Captura a saída do resultado para o histórico
                import io
                import sys

                buffer = io.StringIO()
                sys.stdout = buffer
                executar_operacao(opcao)
                sys.stdout = sys.__stdout__
                saida = buffer.getvalue().strip()
                print(saida)

                # Extrai apenas a linha do resultado para o histórico
                for linha in saida.splitlines():
                    if "✅" in linha:
                        historico.append(linha.replace("✅", "").strip())

            except (ZeroDivisionError, ValueError) as e:
                sys.stdout = sys.__stdout__
                print(f"\n  ❌  {e}")
        else:
            print("\n  ⚠️  Opção inválida. Escolha uma opção do menu.")

        input("\n  Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()
