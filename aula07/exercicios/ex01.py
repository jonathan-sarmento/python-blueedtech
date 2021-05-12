def menor(a, b):
    if a == b:
        print('Valores iguais!')
    else:
        menor = (a+b - abs(a-b))/2
        print(f'Menor = {menor}')


n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
menor(n1, n2)
