
def function(frase): # Função que recebe a frase e faz o tratamento
    vogais = 'AEIOUÁÀÂÃÉÈÊÍÌÎÔÕÓÒÚÙÛaeiouáàâãéèêíìîôõóòúùû'

    for c in frase:
        if c in vogais:
            frase = frase.replace(c, '')

    return frase


frase = input('Digite uma frase: ')
novaFrase = function(frase)

print(novaFrase)
print(f'Quantidade de letras retiradas = {len(frase) - len(novaFrase)}')
