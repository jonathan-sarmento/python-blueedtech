def imc(p, h):
    r = p/(h**2)
    return r

peso = float(input('Digite o peso[Kg]: '))
altura = float(input('Digite a altura[m]: '))

print(f'IMC = {imc(peso, altura):.2f}')