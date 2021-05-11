def salario(vh, ht):
    if ht > 40:
        s = vh*40 + (ht - 40)*1.5*vh
        return s
    else:
        s = vh*ht
        return s

valor_h = float(input('Digite o valor pago por hora de trabalho[R$]: '))
hora_t = int(input('Digite a quantidade de horas trabalhadas: '))

print(f'Salário = R$ {salario(valor_h, hora_t)}')