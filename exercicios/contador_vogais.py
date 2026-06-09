# função que receba uma string e retorne quantas vogais existem nela.


def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador


texto = str(input("Digite uma palavra ou frase: "))
print(f"A quantidade de vogais na frase é: {contar_vogais(texto)}")
