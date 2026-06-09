# %%
import pandas as pd
from IPython.display import display

base = "../../dataset/netflix_titles.csv"
df = pd.read_csv(base)

# mostar todas as colunas
pd.set_option("display.max_columns", None)
df

# display(df.head())

# %%
