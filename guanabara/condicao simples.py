viajem = float(input('Digite a distancia em Km: '))
passagem = 0.50
passagemlonga = 0.40
if viajem <= 200:
    print(f'Sua viajem dará: R${viajem*passagem:.2f}')
elif viajem > 200:
    print(f'Sua viajem dará: R${viajem*passagemlonga:.2f} com desconto')
