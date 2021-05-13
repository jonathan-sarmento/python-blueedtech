
frase = input('Digite uma frase: ')

for c in frase:
    x = c.lower()
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        frase = frase.replace(c, '')

print(frase)