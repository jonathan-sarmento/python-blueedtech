def somaImposto(taxaImposto, custo):
    custo += custo*taxaImposto
    return custo


valor = float(input('Digite o preço do produto[R$]: '))
taxa = float(input('Digite a taxa de imposto[%]: '))

print(f'Valor do produto com imposto: R$ {somaImposto(taxa, valor)}')
