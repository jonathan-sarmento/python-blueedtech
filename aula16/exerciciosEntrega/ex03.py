from os import system
from random import randint
from time import sleep

def load(a):
    system('cls')
    print(f'Carregando{str("."*(a%4))}')
    sleep(0.2)


senha = 'thi.code é o messias!'

while input('Digite a senha: ') != senha:
    print('Senha incorreta! Tente novamente.')

for x in range(0, 9):
    load(x)

system('cls')
sleep(0.5)
print('Bem vindo!')
sleep(0.5)
print('Regras do jogo:')
print('- O computador vai “pensar” em um número entre 0 e 10;')
print('- você vai tentar adivinhar qual número foi escolhido;')
print('- a cada palpite incorreto você receberá uma dica.')
print('Boa sorte!')
print()
input("Pressione ENTER para continuar")
system('cls')
qtpalpites = 1
ncomp = randint(0, 10)

print('Digite o número')
n = int(input('>> '))

while n != ncomp:
    print('Valor incorreto!')
    if n < ncomp:
        print(f'O resultado é maior que {n}')
    elif n > ncomp:
        print(f'O resultado é menor que {n}')
    qtpalpites += 1
    n = int(input('>> '))

print('Você acertou, Parabéns!')
print(f'Quantidade de palpites = {qtpalpites}')
