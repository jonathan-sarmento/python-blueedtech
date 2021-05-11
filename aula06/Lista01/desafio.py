def data(d, m, a):
    if (d > 0 and d <= 30) and (m > 0 and m <= 12) and (a >= 1000 and a <= 9999): # Considerei que, fora Fevereiro, todos os meses tem 30 dias
        if m == 1:
            return 'Janeiro'
        elif m == 2:
            if a%4 == 0 and d <= 29:
                return 'Fevereiro'
            elif d <= 28:
                return 'Fevereiro'
            else:
                return None
        elif m == 3:
            return 'Março'
        elif m == 4:
           return 'Abril'
        elif m == 5:
            return 'Maio'
        elif m == 6:
            return 'Junho'
        elif m == 7:
            return 'Julho'
        elif m == 8:
            return 'Agosto'
        elif m == 9:
            return 'Setembro'
        elif m == 10:
            return 'Outubro'
        elif m == 11:
            return 'Novembro'
        elif m == 12:
            return 'Dezembro'

    else:
        return None    




dia, mes, ano = [int(x) for x in input('Digite a data[DD/MM/AAAA]: ').split('/')]

month = data(dia, mes, ano)

if month == None:
    print('NULL')
else:
    print(f'{dia} de {month} de {ano}')
