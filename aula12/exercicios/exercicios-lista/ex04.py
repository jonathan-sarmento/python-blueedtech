import itertools

njogos = int(input('Digite o número de jogos: '))
jogos = list()

for x in itertools.combinations(range(61), 6):
    aux = list(x[:])
    jogos.append(aux[:])
    if len(jogos) == njogos:
        break

for x in jogos:
    print(x)
