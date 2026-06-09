# %%
import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv')


# %%
# tipos de visualização de amostras

#cabeçalho
df_clientes.head()
#ultimos
df_clientes.tail()
#amostra
df_clientes.sample(10)
#qtd de linhas e coluna (atributo)
df_clientes.shape
#colunas do dataframe
df_clientes.columns
#indices do dataframe
df_clientes.index
#estatisticas / a qtd de memoria usada é uma estimativa
df_clientes.info()
#estatisticas / qtd exata de memoria usada
df_clientes.info(memory_usage='deep')
#tipo de coluna (dtypes mostra a serie)
df_clientes.dtypes
