def maior(a, b, c):
    maior = (a+b + abs(a-b))/2
    maior = (maior+c + abs(maior-c))/2
    return maior


def menor(a, b, c):
    menor = (a+b - abs(a-b))/2
    menor = (menor+c - abs(menor - c))/2
    return menor


def media(a, b=0, c=None):
    if c == None:
        media = (a+b)/2
        return media
    else:
        media = (a+b+c)/3
        return media




nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

print(f'Média considerando as três notas: {media(nota1, nota2, nota3)}')
m = nota1+nota2+nota3 - menor(nota1, nota2, nota3)
print(f'Média com as 2 notas mais altas: {media(m)}')
print(f'Nota mais alta: {maior(nota1, nota2, nota3)}')
print(f'Nota mais baixa: {menor(nota1, nota2, nota3)}')