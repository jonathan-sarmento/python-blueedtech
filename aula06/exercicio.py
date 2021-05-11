def area(a, b):
    """
    -> Funcao area :
    Recebe dois parametros, 
    a - largura
    b - comprimento
    Sem retorno
    """
    area = a*b
    print(f'O valor da área é: {area}m²')


l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))

area(l, c)