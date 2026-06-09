from datetime import date
data_nascimento = int(input('Ano de nascimento: ' ))
ano_atual = date.today().year
idade = date.today().year - data_nascimento
alistamento = 18 - idade
ano_alistamento = alistamento + date.today().year
print(f'Quem nasceu em {data_nascimento} tem {idade} anos em 2021')
if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE')
elif idade >= 18:
    print(f'Você já deveria ter se alistado há {ano_atual-ano_alistamento} anos')
    print(f'Seu alistamento foi em {ano_alistamento}')
elif idade < 18:
    print(f'Ainda faltam {alistamento} ano(s) para o alistamento')
    print(f'Seu alistamento será em {ano_alistamento}')
