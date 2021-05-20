
qt18 = qtm = qtm20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo[M/F]: ').upper().strip()[0]

    if idade >= 18:
        qt18 += 1
    if sexo == 'M':
        qtm += 1
    if sexo == 'F' and idade < 20:
        qtm20 += 1

    continuar = input('Deseja continuar?[s/n]: ').lower().strip()[0]
    if not(continuar == 's'):
        break

print(f'Quantida de pessoas acima de 18 anos = {qt18}')
print(f'Quantidade de homens = {qtm}')
print(f'Quantidade de mulheres com menos de 20 anos = {qtm20}')


