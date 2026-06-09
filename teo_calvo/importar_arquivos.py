# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%
df.to_csv("../data/cliente_2.csv", index=False)

