resposta = list()

resposta.append(input('Telefonou para a vítima?[Sim or Nao]: ').lower())
resposta.append(input('Esteve no local do crime?[Sim or Nao]: ').lower())
resposta.append(input('Mora perto da vítima?[Sim or Nao]: ').lower())
resposta.append(input('Devia para a vítima?[Sim or Nao]: ').lower())
resposta.append(input('Já trabalhou com a vítima?[Sim or Nao]: ').lower())

if resposta.count('sim') == 2:
    print('Suspeita!')
elif resposta.count('sim') == 3 or resposta.count('sim') == 4:
    print('Cúmplice!')
elif resposta.count('sim') == 5:
    print('Assassino!')
else:
    print('Inocente!')
