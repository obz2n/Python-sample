import requests

url = "https://cep.awesomeapi.com.br/json/30140008"
response = requests.get(url)
data = response.json()
print(data)


all_data = []

for cep in range(30140000, 30140010):
    url = f"https://cep.awesomeapi.com.br/json/{cep:08d}"
    response = requests.get(url)
    data = response.json()
    all_data.append(data)