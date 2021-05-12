def ficha(nome, gol):
        print('---FICHA---')
        print(f'Nome do jogador: {nome}')
        print(f'Quantidade de gols marcados: {gol}')

    
name = input('Digite o nome do jogador: ')
gols = int(input('Digite a quantidade de gols marcados: '))
ficha(name, gols)