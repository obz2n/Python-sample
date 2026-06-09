# %%
import pandas as pd
import requests
# %%
# Exemplo: Tratandop dados retornados pela API
url = 'https://api.sampleapis.com/presidents/presidents'
df = pd.DataFrame(requests.get(url).json())
#df[['inicio','fim']] = df.yearsInOffice.str.split(' - ', expand=True)
df

# %%
df_vice = df.explode('vicePresidents')[['name','vicePresidents']]
df_vice
# %%
