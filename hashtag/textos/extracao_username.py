"""
Exercício 4: Extração de Username para Log (Setor de Segurança) Para criar um log de
acessos, o sistema precisa extrair apenas a parte do nome do usuário de um e-mail
corporativo (tudo o que vem antes do @). Dado o e-mail
beatriz.oliveira@grupocorp.com, use a função .find() e o fatiamento de texto
para extrair e exibir apenas o nome beatriz.oliveira.
"""

# Pode ser utilizado o input para receber o e-mail do usuário, exemplo: beatriz.oliveira@grupocorp.com
usuario_email = str(input("Digite o e-mail corporativo: "))


def extrair_username(email: str) -> str:
    pos_arroba = email.find("@")
    if pos_arroba == -1:
        return ""
    return email[:pos_arroba]


print(extrair_username(usuario_email))
