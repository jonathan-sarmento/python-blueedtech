def nota(n):
    if n >= 9:
        return 'A'
    elif n >= 8:
        return 'B'
    elif n >= 7:
        return 'C'
    elif n >= 6:
        return 'D'
    elif n > 4:
        return 'E'
    elif n <= 4:
        return 'F'

    
n = float(input('Digite a nota[0 - 10.0]: '))

print(f'Nota = {nota(n)}')