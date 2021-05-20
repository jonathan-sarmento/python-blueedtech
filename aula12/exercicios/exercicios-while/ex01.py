
op = 0

while op != 5:
    numbers = list()
    numbers.append(float(input('Digite o primeiro valor: ')))
    numbers.append(float(input('Digite o segundo valor: ')))
    op = 0
    while op != 4 and op != 5:
        print('\n[ 1 ] somar')
        print('[ 2 ] multiplicar')
        print('[ 3 ] maior')
        print('[ 4 ] novos valores')
        print('[ 5 ] sair do programa')
        op = int(input('Digite a opção: '))

        if op == 1:
            print(f'{numbers[0]} + {numbers[1]} = {sum(numbers)}')
        elif op == 2:
            print(f'{numbers[0]} * {numbers[1]} = {numbers[0]*numbers[1]}')
        elif op == 3:
            print(f'Maior = {max(numbers)}')
        elif op == 4 or op == 5:
            continue
        else:
            print('Opção inválida!')
