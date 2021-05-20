
total = qtp1000 = 0
pbarato = list()

while True:
    produto = list()
    produto.append(input('Digite o nome do produto: '))
    produto.append(float(input('Digite o valor do produto[R$]: ')))
    if total == 0:
        pbarato = produto[:]
    if produto[1] > 1000:
        qtp1000 += 1
    if produto[1] < pbarato[1]:
        pbarato = produto[:]

    total += produto[1]

    continuar = input('Deseja continuar?[s/n]: ').lower().strip()[0]
    if not(continuar == 's'):
        break

print(f'Total gasto na compra = R$ {total}')
print(f'Quantidade de produtos com o valor acima de R$1000: {qtp1000}')
print(f'Produto mais barato = {pbarato[0]}')
