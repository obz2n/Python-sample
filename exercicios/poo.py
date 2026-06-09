# exemplo de classe carro


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


class CarroPopular(Carro):
    def __init__(self, marca, modelo, ano, preco):
        super().__init__(marca, modelo, ano)
        self.preco = preco

    def exibir_informacoes(self):
        # herança do método exibir_informacoes
        super().exibir_informacoes()
        print(f"Preço: {self.preco}")


mustang = Carro("Ford", "Mustang", 2022)
mustang.exibir_informacoes()
celta = CarroPopular("Chevrolet", "Celta", 2010, 20000)
celta.exibir_informacoes()
gol = CarroPopular("Volkswagen", "Gol", 2015, 30000)
gol.exibir_informacoes()
astra = CarroPopular("Opel", "Astra", 2018, 40000)
astra.exibir_informacoes()
