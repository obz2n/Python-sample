"""
Dicionários são listas de valores com rotulos
Separados em chave e valor
"""

emails_gerentes = {
    "Iguatemi": "iguatemi@empresa.com",
    "Plaza": "plaza@empresa.com",
    "Barra": "barra@gmail.com",
}


# se quiser descobrir qual o e-mail do shopping 'Iguatemi'
email = emails_gerentes["Iguatemi"]
print(email)

# se quiser descobrir todos os shopping que tem
for shopping in emails_gerentes:
    print(shopping)

# se quiser descobrir todos os e-mails dos gerentes
for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print(email)
