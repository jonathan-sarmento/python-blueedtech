
''' Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar. No final mostre:
    Quantas pessoas foram cadastradas
    Mostre o maior peso
    Mostre o menor peso
'''
from os import system

dados = list()
menor = maior = 0

while True:
    aux = list()
    aux.append(input('Digite o nome: '))
    aux.append(float(input('Digite o peso[Kg]: ')))
    dados.append(aux[:])
    if len(dados) == 1:
        menor = maior = aux[1]
    if aux[1] > maior:
        maior = aux[1]
    if aux[1] < menor:
        menor = aux[1]

    if not input('Deseja continuar?[s/n]: ').lower() == 's':
        break

m = dados[:][1]
print(m)
# system('cls')
print(f'Quantidade de pessoas cadastradas = {len(dados)}')
print(f'Maior peso = {maior} Kg')
print(f'Menor peso = {menor} Kg')

