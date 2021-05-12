def function(a, b, l):
    if a+b > l:
        return 'True'
    else:
        return 'False'


n1 = float(input('Digite o primero número: '))
n2 = float(input('Digite o segundo número: '))
limite = float(input('Digite limite: '))

print(f'{function(n1, n2, limite)}')
