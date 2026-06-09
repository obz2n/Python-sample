# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

series_idades = pd.Series(idades)

media_idades = series_idades.mean()
print("media:" ,media_idades)

variancia_idades = series_idades.var()
print("variancia:" ,variancia_idades)

sumary_idades = series_idades.describe()
print("sumary:" ,sumary_idades)


series_idades = pd.Series(idades)
print(idades)

# %%
series_idades = series_idades.sort_values()
series_idades

# %%
series_idades.iloc[0]
series_idades[0]
series_idades.iloc[:3]
