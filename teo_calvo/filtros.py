# %%
import pandas as pd
df = pd.read_csv('../data/transacoes.csv')
df.head(5)

# %%
pontos = [10, 20, 30 ,40 
          ,50 ,60, 70, 80 ,90, 100]
filtro = []
valores_acima_50 = []                              
for i in pontos:
    if i >=50:
        filtro.append(i)
        #filtro.append(i>=50)
valores_acima_50
filtro

# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo","nah","mah"],
        "idade": [18, 30, 45],
        "uf": ["sp","rj","ce"],
    }
)
#filtro = brinquedo["idade"] == 30pint
print(brinquedo)


# %%
#qtd de pontos acima de 50

df = pd.read_csv('../data/transacoes.csv')
df.head(5)
pontos_acima_50 = df['qtdePontos'] >= 50
df[pontos_acima_50]
# %%
#qtd de pontos acima de 50 e menor que 100
#and == & ou '*'
acima_50_abaixo_100 = (df['qtdePontos'] >= 50) & (df['qtdePontos'] < 100) & (df['dtCriacao'] == '2024-11-11 12:36:33.625')
df[acima_50_abaixo_100]

# %%
#utilizando ou com '|', '+'acima_50_ou_abaixo_
#or == | ou '+'
acima_50_ou_100 = (df['qtdePontos'] == 50) | (df['qtdePontos'] == 100)
df[acima_50_ou_100]

# %%

filtro = (df['qtdePontos'] > 0) & (df['qtdePontos'] <=50) & (df['dtCriacao'] >= '2025-01-01')
df[filtro] 

