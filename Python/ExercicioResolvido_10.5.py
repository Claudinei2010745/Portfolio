# Considere o seguinte conjunto de dados: Nome + (N1, N2, N3, N4). Nome representa o nome de um
# aluno e deve ser usado como chave. N1, N2, N3, N4 representam as notas de provas desse aluno.
# Escreva um programa que leia os dados de Q alunos e determine a situação de cada aluno. O critério
# que garante a aprovação é que a média aritmética das 4 notas de prova seja maior ou igual 6,0. Q é
# a quantidade de alunos e este valor deve ser lido do teclado no começo do programa.
# Para cada aluno o nome deve ser lido em separado e suas notas de prova devem ser lidas juntas na
# mesma linha, com um espaço em branco de separação.
# Para cada aluno o programa deve mostras o Nome, as 4 notas de prova, a média final e a situação
# (aprovado/reprovado). As notas devem ser exibidas com uma casa decimal.

alunos = {}
Q = int(input('Digite a quantidade de alunos: '))
for i in range(Q):
    nome = input(f'   nome do aluno {i+1} >> ')
    notas = input(f'   notas do {nome} >> ')
    notas = notas.split()
    for j in range (len(notas)):
      notas[j] = float(notas[j])
    alunos[nome] = tuple(notas)

print('\nResultado da Turma')
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    if media >= 6.0:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    print('{:12} {:4.1f} {:4.1f} {:4.1f} {:4.1f} {} com média = {:4.1f}'.format(
        nome,
        notas[0],
        notas[1],
        notas[2],
        notas[3],
        situacao,
        media)
    )
    print('_______________')
print('Fim do Programa')


