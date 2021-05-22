aluno = dict()

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input('Digite a média do aluno[0-10]: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 >= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'

for x in aluno:
    print(f'{x}: {aluno[x]}')