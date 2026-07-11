"""
Exercício 3: Migração de Servidor de E-mail (Setor de TI) Sua empresa mudou de nome
e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o
domínio @grupocorp.com. O e-mail do funcionário é andre_silva@empresa.com.br.
Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo
endereço de e-mail.
"""

novo_dominio = "@grupocorp.com"
antigo_dominio = "@empresa.com.br"

antigo_email = "andre_silva@empresa.com.br"

novo_email = antigo_email.replace(antigo_dominio, novo_dominio)
print("=" * 60)
print(f"antigo_email: {antigo_email}")
print(f"novo_email: {novo_email}")
print("=" * 60)
