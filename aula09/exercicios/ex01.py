
l = [5, 7, 2, 9, 4, 1, 3]

print(f'Tamanho da lista = {len(l)}')
print(f'Maior valor da lista = {max(l)}')
print(f'Menor valor da lista = {min(l)}')
print(f'Soma de todos os elementos = {sum(l)}')
l.sort()
print(f'Lista em ordem crescente: {l}')
l.sort(reverse=True)
print(f'Lista em ordem decrescente = {l}')

