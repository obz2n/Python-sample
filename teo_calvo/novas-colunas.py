# %%
import pandas as pd

df = pd.read_csv('../data/clientes.csv')
df 

# %%
# exemplo de acrescimo utilizando for

nova_coluna = []
for i in df['qtdePontos']:
    nova_coluna.append(i + 100)

nova_coluna

# exemplo de acrescimo utilizando series
df['qtdePontos'] + 100
# %%
df['emailtwith'] = df['flEmail'] + df['flTwitch']
acima_de_1 = df['emailtwith'] >= 1
df[acima_de_1]

# %%

# soma de redes sociais dos clientes
df['somaRedes'] = df['flEmail'] + df['flTwitch'] + df['flInstagram'] + df['flYouTube'] + df['flBlueSky']
df
# %%
# cliente com todas as redes sociais
cliente_com_todas = df['somaRedes'] == 5
df[cliente_com_todas]
# %%
top_pontos = df.nlargest(10, 'qtdePontos')
top_pontos
# %%
df['qtdePontos'].describe()