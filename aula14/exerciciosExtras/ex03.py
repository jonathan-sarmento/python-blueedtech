word = input('digite uma palvra: ').lower().replace(' ', '')

if word == word[::-1]:
    print('Esta frase é um palíndromo') 
else:
    print('Esta frase não é um palíndromo')
