# %%
import pandas as pd


idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

media = sum(idades) / len(idades)
print("Media:",media) 

diffs = 0
for i in idades:
    diffs += (i - media) ** 2
variancia = diffs / len(idades)-1
print("Variancia:",variancia) 

# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

series_idades = pd.Series(idades)
