
numbers = [[], []]

for x in range(0, 7):
    num = int(input('Digite um valor inteiro: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)

numbers[0].sort()
numbers[1].sort()
print(f'Valores pares = {numbers[0]}')
print(f'Valores ímpares = {numbers[1]}')
