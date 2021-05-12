from unicodedata import normalize

def custo_hotel(noites):
    return noites*140


def custo_aviao(cidade):
    if cidade == 'sao paulo':
        return 312
    elif cidade == 'porto alegre':
        return 447
    elif cidade == 'recife':
        return 831
    elif cidade == 'manaus':
        return 986
    else:
        return 0


def custo_carro(dias):
    if dias >= 3 and dias < 7:
        custo = 40*dias - 20
        return custo
    elif dias >= 7:
        custo = 40*dias - 50
        return custo
    else:
        custo =  40*dias
        return custo


def custo_total(cidade, dias=0, extra=0):
    custo = custo_hotel(dias) + custo_aviao(cidade) + custo_carro(dias) + extra
    return custo


city = input('Digite o nome da cidade: ').lower()
city = normalize('NFKD', city).encode('ASCII','ignore').decode('ASCII') # Tirar qualquer possível acento da frase

days = int(input('Digite o número de dias: '))
extra = float(input('Digite o valor extra[R$]: '))
print(f'Custo total = R$ {custo_total(city, days, extra)}')
