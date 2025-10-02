
traco = f'\33[33m{'-'*45}\33[m'
print(traco)
jogo = 'Jogo: pedra, papel e tesoura (2 jogadores)'
print(f'\33[32m{jogo}\33[m')
print(f'{traco}')
while True:
    print('''Escolham entre:
pedra
papel
tesoura''')
    print(traco)
    jogada_jogador1 = 0
    jogada_jogador2 = 0
    jogar_de_novo = 0
    while jogada_jogador1 not in ('pedra', 'papel', 'tesoura'):
        jogada_jogador1 = input(f'Jogador 1, qual você escolhe?\n').strip().lower()
        if jogada_jogador1 in ('pedra', 'papel', 'tesoura'):
            break
        print(f'\33[31m{'Escolha uma opção válida'}\33[m')
    while jogada_jogador2 not in ('pedra', 'papel', 'tesoura'):
        jogada_jogador2 = input(f'Jogador 2, qual você escolhe?\n').strip().lower()
        if jogada_jogador2 in ('pedra', 'papel', 'tesoura'):
            break
        print(f'\33[31m{'Escolha uma opção válida'}\33[m')
    print(traco)
    if (jogada_jogador1=='pedra' and jogada_jogador2=='tesoura') or (jogada_jogador1=='tesoura'
    and jogada_jogador2=='papel') or (jogada_jogador1=='papel' and jogada_jogador2=='pedra'):
        print('Jogador 1 venceu!')
        if jogada_jogador1=='pedra' and jogada_jogador2=='tesoura':
            print('Pedra quebra tesoura!')
        elif jogada_jogador1=='tesoura' and jogada_jogador2=='papel':
            print('Tesoura corta papel!')
        elif jogada_jogador1 == 'papel' and jogada_jogador2 == 'pedra':
            print('Papel enrola pedra!')
    if jogada_jogador1=='pedra' and jogada_jogador2=='papel':
        print('Jogador 2 venceu!')
        print('Papel enrola pedra!')
    elif jogada_jogador1=='papel' and jogada_jogador2=='tesoura':
        print('Jogador 2 venceu!')
        print('Tesoura corta papel!')
    elif jogada_jogador1=='tesoura' and jogada_jogador2=='pedra':
        print('Jogador 2 venceu!')
        print('Pedra quebra tesoura!')
    else:
        print('Empatou!')
    print(traco)
    jogar_de_novo = int(input('''Querem jogar de novo?
1 - Sim
2 - Não
'''))
    print(f'\33[34m{'x'*40}\33[m')
    if jogar_de_novo == 2:
        break
# print(traco)
print('Fim de Jogo')

