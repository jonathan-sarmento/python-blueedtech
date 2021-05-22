from time import sleep
from random import randint
from operator import itemgetter

dicio = dict()
for x in range(1, 5):
    dicio[str(f'Jogador{x}')] = randint(1, 6)
    print(f'Jogador{x} = {dicio[str(f"Jogador{x}")]}')
    sleep(1)

print('-'*15)

rank = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print('Ranking:')
for p, x in enumerate(rank):
    print(f'{p+1}° lugar - {x[0]} = {x[1]}')
