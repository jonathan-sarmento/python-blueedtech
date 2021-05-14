
n = int(input('Digite o número de matérias: '))
notas = list()
for x in range(0, n):
    notas.append(float(input(f'Digite a nota {x+1}: ')))

print(f'Média geral = {(sum(notas)/n):2f}')
