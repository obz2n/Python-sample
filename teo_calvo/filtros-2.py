# %%
import pandas as pd
df = pd.read_csv('../data/transacao_produto.csv')
df

# %%
filtro = (df['idProduto'] == 5) | (df['idProduto'] == 11) 
df

# %%
#isin é parecido com IN do SQL
df['idProduto'].isin([5,11])
df[filtro]
# %%
#valores não nulos (NA e NULO)
clientes = pd.read_csv('../data/clientes.csv')
clientes.head()
filtro= clientes['dtCriacao'].isna()
clientes[filtro]
# %%
#negacao da condicao (usasse o ~, comparacao entre "isna()" e "notna()"
~clientes['dtCriacao'].isna() #aqui busca o NA"
clientes['dtCriacao'].notna() #Aqui nega o NA

# %%
#filtros view
df = pd.read_csv('../data/clientes.csv')
clientes.head()

filtro = clientes['qtdePontos'] == 0
clientes[filtro]
# %%
#utilizando copy para imagem diferente

A = [1,2]
B = A.copy()
print('A:', A)
print('B:', B)

B.append('teste')
print('A:', A) 
print('B:', B)