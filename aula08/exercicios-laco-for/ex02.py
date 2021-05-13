
frase = input('Digite uma frase: ').lower()

a = e = i = o = u = 0

for x in frase:
    if x == 'a':
        a += 1
    elif x == 'e':
        e += 1
    elif x == 'i':
        i += 1
    elif x == 'o':
        o += 1
    elif x == 'u':
        u += 1

print(f'Quantidades de a: {a}')
print(f'Quantidades de e: {e}')
print(f'Quantidades de i: {i}')
print(f'Quantidades de o: {o}')
print(f'Quantidades de u: {u}')

