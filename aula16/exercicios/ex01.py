
n1 = float(input('Digite o primero número: '))
n2 = float(input('Digite o segundo número: '))

if (n1 + n2)%2 == 0:
    paridade = 'Soma par'  
else:
    paridade = 'Soma ímpar'
print(f'{n1} + {n2} = {n1+n2}[{paridade}]')
print(f'{n1} * {n2} = {n1*n2}')
print(f'{n1} // {n2} = {n1//n2}')
print(f'Maior = {max([n1, n2])}')

if n1*n2 > 40:
    if n1 // n2 == 0:
        print(f'Divisão inteira entre {n1} e {n2} é 0, não foi possível concluir a operação!')
    else:
        print(f'{(n1*n2)/(n1//n2):.2f}')
else:
    print(f'A multiplicação entre {n1} e {n2} não foi maior que 40')
