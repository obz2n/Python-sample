# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

filtro = clientes['qtdePontos'] == 0
clientes[filtro]
clientes['flag_1'] = 1
clientes

# %%
# Variáveis são como referências a objetos
A = [1,2]
B = A.copy() # cria uma cópia para isolar a variavel
print('A:', A)
print('B:', B)

B.append('view')
print('A:', A)
print('B:', B)