# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

# print("\n******************* Calculadora em Python *******************")
# print(''' Opções:
# 1 - Adição
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão''')
# print('-'*20)
# while True:
#     try:
#         opções = int(input('Selecione a opção desejada: '))
#         if opções < 5 and opções > 0:
#             break
#         else:
#             print('Digite uma opção correta.')
#     except ValueError:
#         print('Digite uma opção correta.')
# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite um número: '))
# print('-'*20)
# if opções == 1:
#     print('Você escolheu Adição!')
#     soma = num1 + num2
#     print(f'{num1}+{num2} = {soma}')
# elif opções == 2:
#     print('Você escolheu Subtração!')
#     subtração = num1 - num2
#     print(f'{num1}-{num2} = {subtração}')
# elif opções == 3:
#     print('Você escolheu Multiplicação!')
#     multiplicao = num1 * num2
#     print(f'{num1}*{num2} = {multiplicao}')
# elif opções == 4:
#     print('Você escolheu Divisão!')
#     divisao = num1 / num2
#     print(f'{num1}/{num2} = {divisao}')


print("\n******************* Calculadora em Python *******************")

def calculadora():
    print(''' Opções:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potencia''')
    print('-' * 20)
    while True:
        try:
            opções = int(input('Selecione a opção desejada: '))
            if opções < 6 and opções > 0:
                break
            else:
                print('Digite uma opção correta.')
        except ValueError:
            print('Digite uma opção correta.')
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    soma = num1 + num2
    subtração = num1 - num2
    multiplicação = num1 * num2
    divisão = num1 / num2
    potencia = num1 ** num2
    print('-' * 20)
    if opções == 1:
        print('Você escolheu Adição!')
        print(f'{num1}+{num2} = {soma}')
    elif opções == 2:
        print('Você escolheu Subtração!')
        print(f'{num1}-{num2} = {subtração}')
    elif opções == 3:
        print('Você escolheu Multiplicação!')
        print(f'{num1}*{num2} = {multiplicação}')
    elif opções == 4:
        print('Você escolheu Divisão!')
        print(f'{num1}/{num2} = {divisão}')
    elif opções == 5:
        print('Você escolheu Potencia!')
        print(f'{num1}**{num2} = {potencia}')



calculadora()

