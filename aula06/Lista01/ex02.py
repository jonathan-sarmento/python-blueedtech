def result(num):
    if num > 0:
        return 'P'
    elif num < 0:
        return 'N'
    elif num == 0:
        return '0'


num = float(input('Digite um numero: '))

print(f'{result(num)}')