from datetime import datetime

anoAtual = datetime.now().year
pessoa = dict()

pessoa['nome'] = input('Digite o nome: ')
pessoa['idade'] = anoAtual- int(input('Digite o ano de nascimento: '))
pessoa['ctps'] = int(input('Digite a CTPS[xxxxxxxxxxx]: '))
if pessoa['ctps'] != 0:
    pessoa['ano de contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o salário[R$]: '))
    pessoa['idade aposentadoria'] = pessoa['idade'] + 35 -(anoAtual - pessoa['ano de contratacao'])

for k, v in pessoa.items():
    if k == 'idade aposentadoria':
        print(f'Você poderá se aposentar a partir dos {v} anos')
    elif k == 'salario':
        print(f'{k.capitalize()}: R$ {v}')
    else:
        print(f'{k.capitalize()}: {v}')