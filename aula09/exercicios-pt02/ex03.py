
result = list()

for x in range(0, 15):
    result.append(input('Digite o seu estado civil[Casado ou Solteiro]: ').lower())

casado = result.count('casado')
solteiro = 15 - casado
print(f'Quantidade de casados(as) = {casado}')
print(f'Quantidade de solteiros(as) = {solteiro}')
