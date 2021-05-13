
n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = int(input('Digite n3: '))
n4 = int(input('Digite n4: '))

tupla = (n1, n2, n3, n4)
print(f'Quantidade de 9: {tupla.count(9)}')

if (3 in tupla) == False:
    print('O número 3 não foi encontrado na tupla!')
else:
    print(f'Índice do número 3: {tupla.index(3)}')
