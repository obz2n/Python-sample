'''
Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de
serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o
valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
1.​ Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
2.​ Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
3.​ Converter para número decimal (float).
4.​ Calcular o valor do imposto (15% do valor bruto).
5.​ Exibir uma mensagem formatada com f-string mostrando o valor do imposto com
duas casas decimais.
'''

from decimal import Decimal, InvalidOperation


def ler_valor_bruto() -> Decimal:
    valor_digitado = input("Digite o valor bruto (ex.: R$ 5.000,00): ").strip()
    valor_limpo = valor_digitado.replace("R$", "").replace(".", "").replace(",", ".").strip()

    try:
        return Decimal(valor_limpo)
    except InvalidOperation as exc:
        raise ValueError("Valor inválido. Digite um valor monetário válido.") from exc


def calcular_imposto(valor_bruto: Decimal) -> Decimal:
    return valor_bruto * Decimal("0.15")


def formatar_moeda(valor: Decimal) -> str:
    return f" {valor:.2f}"


def main() -> None:
    print("=" * 30)
    print("Calculadora de Impostos sobre Vendas")
    print("=" * 30)

    try:
        valor_bruto = ler_valor_bruto()
    except ValueError as exc:
        print(exc)
        return

    valor_imposto = calcular_imposto(valor_bruto)
    print(f"O valor do imposto sobre vendas é: {formatar_moeda(valor_imposto)}")


if __name__ == "__main__":
    main()
