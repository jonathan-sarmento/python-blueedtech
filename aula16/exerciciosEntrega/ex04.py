def validacao(dia, mes, ano): # Função que valida a data
    if (0 < dia <= 30) and (0 < mes <= 12) and ( 1000 <= ano <= 9999):
        return True
    else:
        return False

# Considerei que os dias vão até 30 e não existe ano bissexto
meses = [0, 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dia, mes, ano = [int(x) for x in input('Digite a data[DD/MM/AAAA]: ').split('/')] # Lê a data no formato DD/MM/AAAA

if validacao(dia, mes, ano):
    print(f'{dia} de {meses[mes]} de {ano}')
else:
    print('Data inválida!')

