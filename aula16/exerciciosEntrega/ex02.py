
frase = input('Digite uma frase: ')

vogais = 'AEIOUÁÀÂÃÉÈÊÍÌÎÔÕÓÒÚÙÛaeiouáàâãéèêíìîôõóòúùû'
a = e = i = o = u = 0

for c in frase:
    if c in 'AÁÀÂÃaáàâã':
        a += 1
    elif c in 'EÉÈÊeéèê':
        e += 1
    elif c in 'IÍÌÎiíìî':
        i += 1
    elif c in 'OÔÕÓÒoôõóò':
        o += 1
    elif c in 'UÚÙÛuúùû':
        u += 1

    if c in vogais:
        frase = frase.replace(c, '')

print(f'Quantidade de A = {a}')
print(f'Quantidade de E = {e}')
print(f'Quantidade de I = {i}')
print(f'Quantidade de O = {o}')
print(f'Quantidade de U = {u}')
print(f'Frase sem as vogais: {frase}')
