pessoas = list()
mulheres = list()
idadesA = list()
pessoa = dict()
media = 0

while True:
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['sexo'] = input('Digite o sexo[M/F]: ').upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('Sexo inválido!')
        pessoa['sexo'] = input('Digite o sexo[M/F]: ').upper().strip()[0]
    pessoa['idade'] = int(input('Digite a idade: '))
    media += pessoa['idade']
    pessoas.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        pessoa['sexo'] = 'Feminino'
        mulheres.append(pessoa.copy())
    
    continuar = input('Deseja continuar?[sim/nao]: ').lower()
    while continuar != 'sim' and continuar != 'nao':
        print('Opção inválida!')
        continuar = input('Deseja continuar?[sim/nao]: ').lower()

    if continuar == 'nao':
        break

media /= len(pessoas)
for x in pessoas:
    if x['idade'] > media:
        idadesA.append(x.copy())

print('-'*20)
print(f'Quantidade de pessoas cadastradas = {len(pessoas)}')
print(f'Média de idade = {int(media)} anos')
print(f'Lista de mulheres cadastradas: ')
for x in mulheres:
    for k, v in x.items():
        print(f'{k}: {v}')
    print('-'*10)

print('Lista das pessoas com idade acima da média:')
for x in idadesA:
    for k, v in x.items():
        print(f'{k}: {v}')
    print('-'*10)
