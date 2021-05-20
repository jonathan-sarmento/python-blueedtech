
matriz = [[], [], []]
j = 0
i = 0
soma = soma3c = 0
while i < 3:
    while j < 3:
        matriz[i].append(int(input('Digite o valor: ')))
        j += 1
    i += 1
    j = 0

for x in matriz:
    print(f'[ {x[0]} ][ {x[1]} ][ {x[2]} ]')
    soma += sum(x)
    soma3c += x[2]
    
maior = max(matriz[1])
print(f'Soma de todos os valores = {soma}')
print(f'soma da terceira coluna = {soma3c}')
print(f'Maior valor da segunda linha = {maior}')