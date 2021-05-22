
sim = 0

print('Responda sim ou nao:')
if input('Telefonou para a vítima?: ').lower()[0] == 's':
    sim += 1
if input('Esteve no local do crime?: ').lower()[0] == 's':
    sim += 1
if input('Mora perto da vítima?: ').lower()[0] == 's':
    sim += 1
if input('Devia para a vítima?: ').lower()[0] == 's':
    sim += 1
if input('Já trabalhou com a vítima?: ').lower()[0] == 's':
    sim += 1

if sim == 2:
    print('Suspeita!')
elif 3 <= sim <= 4:
    print('Cúmplice!')
elif sim == 5:
    print('Assassino!')
else:
    print('Inocente!')
