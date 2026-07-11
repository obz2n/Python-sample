"""
Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing) O marketing
quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo: lucas
ferreira souza. Você deve extrair apenas o primeiro nome para usar na saudação (ex:
"Olá, Lucas!"). O código deve:
1.​ Encontrar a posição do primeiro espaço.
2.​ Fatiar o texto para pegar apenas o primeiro nome.
3.​ Formatar o nome com a primeira letra maiúscula.
4.​ Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"
"""

nome_completo = "lucas ferreira souza"


def extrair_primeiro_nome(nome: str) -> str:
    pos_espaco = nome.find(" ")
    if pos_espaco == -1:
        return nome.capitalize()
    primeiro_nome = nome[:pos_espaco]
    return primeiro_nome.capitalize()


print(f"Olá, {extrair_primeiro_nome(nome_completo)}!")
