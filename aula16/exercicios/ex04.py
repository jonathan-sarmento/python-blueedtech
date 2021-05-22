def mesExtenso(mes): # Função que retorna o mes por extenso
    if mes == 1:
        return 'Janeiro'
    elif mes == 2:
        return 'Fevereiro'
    elif mes == 3:
        return 'Março'
    elif mes == 4:
        return 'Abril'
    elif mes == 5:
        return 'Maio'
    elif mes == 6:
        return 'Junho'
    elif mes == 7:
        return 'Julho'
    elif mes == 8:
        return 'Agosto'
    elif mes == 9:
        return 'Setembro'
    elif mes == 10:
        return 'Outubro'
    elif mes == 11:
        return 'Novembro'
    else:
        return 'Dezembro'


def validacao(dia, mes, ano): # Função que valida a data
    if (0 < dia <= 30) and (0 < mes <= 12) and ( 1000 <= ano <= 9999):
        return True
    else:
        return False

# Considerei que os dias vão até 30 e não existe ano bissexto
data = list()
data = [int(x) for x in input('Digite a data[DD/MM/AAAA]: ').split('/')]

if validacao(data[0], data[1], data[2]):
    data[1] = mesExtenso(data[1])
    print(f'{data[0]} de {data[1]} de {data[2]}')
else:
    print('Data inválida!')

