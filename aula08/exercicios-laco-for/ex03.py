
n = int(input('Informe um número:'))
print('Divisores:')
for x in range(1, n+1):
    if n%x == 0:
        print(x)

