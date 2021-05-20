
v = vn = vb = 0
c1 = c2 = c3 = c4 = 0

print('1 - Ju')
print('2 - Bi')
print('3 - Leu')
print('4 - Thi.code')
print('5 - Voto Nulo')
print('6 - Voto em Branco')
print('7 - Parar programa e calcular os votos')

while v != 7:
    v = int(input('Digite o número: '))
    
    if v == 1:
        c1 += 1
    elif v == 2:
        c2 += 1
    elif v == 3:
        c3 += 1
    elif v == 4:
        c4 += 1
    elif v == 5:
        vn += 1
    elif v == 6:
        vb += 1

vt = c1 + c2 + c3 + c4 + vn + vb
print('\nVOTOS:')
print(f'Total de votos = {vt}')
print(f'Ju = {c1} ({(100*c1/vt):.2f}%)')
print(f'Bi = {c2} ({(100*c2/vt):.2f}%)')
print(f'Leu = {c3} ({(100*c3/vt):.2f}%)')
print(f'Thi.code = {c4} ({(100*c4/vt):.2f}%)')
print(f'Votos Nulos = {vn} ({(100*vn/vt):.2f}%)')
print(f'Votos em Branco = {vb} ({(100*vb/vt):.2f}%)')