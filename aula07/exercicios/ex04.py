import datetime

x = datetime.datetime.now()

def voto(ano):
    data_atual = x.year
    idade = data_atual - ano
    if idade < 16:
        return 'NEGADO'
    elif idade >= 16 and idade < 18:
        return 'OPCIONAL'
    elif idade >=18:
        return 'OBRIGATORIO'


n = int(input('Digite o ano de nascimento: '))
print(f'IDADE = {x.year - n}')
print(f'VOTO = {voto(n)}')


