'''

classe = Classes em Python são moldes que definem atributos (dados) e métodos (comportamentos) para criar objetos
__init__ = consultor que serve para criar a funcionalidade inicial que a classe terá
self = acessar as propriedades de uma instância
instância = é um objeto individual criado a partir de uma classe

'''


# Modelo para criar novas instancias
# marca, memoria ram, placa de video
import pandas as pd
class computador:
    def __init__(self):
        self.marca = 'Positivo'
        self.memoria_ram = '2gb'
        self.placa_video = 'nvidia'
    pass

# instancias
computador1 = computador()
# print(computador1.marca)
computador2 = computador()
computador3 = computador()
print(computador1.marca, computador1.memoria_ram, computador3.placa_video)


# Deixando a classe dinâmica
class computador:
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video    
    pass

# instancias
computador1 = computador('asus','4gb','nvidia')
computador2 = computador('positivo','12gb','geforce')
computador3 = computador('dell','8gb','atm')
print(computador1.marca, computador1.memoria_ram, computador1.placa_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_video)

# Criando metodos
class computador:
    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video    
    def ligar(self):
        print('Ligando o computador')

    def desligar(self):
        print('Desligando o computador')

    def exibir_informacoes(self):
        print(self.marca, self.memoria_ram, self.placa_video)

# instancias
computador1 = computador('asus','4gb','nvidia')
computador1.ligar()
computador1.desligar()
computador1.exibir_informacoes()
