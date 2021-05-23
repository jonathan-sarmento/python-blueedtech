num = list()

while True:
    num.append(int(input('>> ')))
    continuar = input('Deseja continuar?[s/n]:').lower()[0]
    if not continuar == 's':
        break
    
num.sort(reverse=True)
print('-'*20)
print(f'Foram digitados {len(num)} número(s)')
print('Lista ordenada em ordem decrescente:')
print(num)
if num.count(5) == 0:
    print('O número 5 não está na lista')
else:
    print('O número 5 está na lista')
