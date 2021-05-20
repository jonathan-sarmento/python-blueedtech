matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input('Digite o valor: ')))

for x in matriz:
    print(f'[ {x[0]} ][ {x[1]} ][ {x[2]} ]')
