"""
Exercício 2: Padronização de Dados de CRM (Setor de Vendas) Um vendedor cadastrou
um cliente com os dados desorganizados no sistema: nome = " mArCoS aNtOnIo
rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". Para evitar duplicidade e erros
de envio, você deve:
1.​ Remover os espaços extras no início e fim das duas variáveis.
2.​ Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo
(formato de nome próprio).
3.​ Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.
"""

nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "


def remover_espacos():
    nome.strip()
    email.strip()
    return nome, email


def padronizar_nome(nome):
    return nome.title()


def padronizar_email(email):
    return email.lower()


nome, email = remover_espacos()
nome = padronizar_nome(nome)
email = padronizar_email(email)

print(f"Nome: {nome}")
print(f"Email: {email}")
