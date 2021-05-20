from random import randint

n = randint(0, 10)
tentativa = 1

while int(input('Digite o número: ')) != n:
    print('Número errado, tente novamente')
    tentativa += 1

print(f'Resposta = {n}')
print(f'Quantidade de tentativas = {tentativa}')

