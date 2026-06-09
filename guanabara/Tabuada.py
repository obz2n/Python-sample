num = int(input('Digite um número para ver sua tabuada: '))
print("=" * 12)
x = 1
while x <= 10:
    print(f'{num} x {x} = {num*x}')
    x = x + 1
