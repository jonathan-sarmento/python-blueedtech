numbers = [[], []]

for x in range(0, 7):
    n = int(input('Digite o número: '))
    if n%2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

numbers[0].sort()
numbers[1].sort()
print(f'Pares = {numbers[0]}')
print(f'Ímpares = {numbers[1]}')