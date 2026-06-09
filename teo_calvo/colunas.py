# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv')
df

# %%
#informacoes
df.shape
df.info(memory_usage='deep')
df.dtypes

# %%
#renomear coluna
renamed_colluns={"qtdePontos":"qtPontos",
                        "descSistemaOrigem":"descSistema"}
df.rename(columns=renamed_colluns, inplace=True)
df

# %%
#acessar colunas
df[['idCliente','qtPontos']]

# %%
#acessar colunas com limitação de linha
df[['idCliente','qtPontos']].head(5)

# %%
#reordenar as colunas manualmente
df[['qtPontos','idCliente']].head(5)

# %%
#reordenando asc
colunas = list(df.columns)
colunas.sort()
colunas
# %%
df[colunas]