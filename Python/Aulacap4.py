# #variável global
# saudacao = 'Olá mundo!'
# nome = 'Aluno DSA'
#
# #Função
# def minha_funcao_dsa():
#     #variável local
#     nome = 'Ana'
#     print(f'\nDentro da função: {nome}') # executa a variável dentro da função
#     print(f'\nAcessando a variável global de dentro da função: {saudacao}')
#
# minha_funcao_dsa()
# print(f'\nFora da função: {saudacao}')
# print(f'\nFora da função: {nome}') # executa a variável que está fora da função
#
# # função
# def minha_funcao_dsa():
#     # variável local
#     nome_local = 'Ana'
#     print(f'\nDentro da função: {nome}') # executa a variável fora da função porque não existe igual
#     print(f'\nAcessando a variável global dentro da função: {saudacao}')
#
# minha_funcao_dsa()
# # tentar acessar a variável local fora da função resultará em erro
# # print(f'Tentando acessar "nome" fora da função: {nome_local}')

# TIPOS DE DADOS PRIMITIVOS
# integer (inteiro)
# numero_inteiro = 100
# print(f'Valor: {numero_inteiro}, Tipo: {type(numero_inteiro)}')
# # float
# numero_decimal = 19.99
# print(f'Valor: {numero_decimal}, Tipo: {type(numero_decimal)}')
# # string
# texto = 'Python é incrível'
# print(texto)
# print(f'Valor: {texto}, Tipo: {type(texto)}')
# # boolean (booleano)
# verdadeiro = True
# falso = False
# print(f'Valor: {verdadeiro}, Tipo: {type(falso)}')
# print(f'Valor: {falso}, Tipo: {type(falso)}')

# OPERADORES LÓGICOS
# Usados para combinar expressões booleanas
# Definição de variáveis
tem_dinheiro = True
tem_tempo = False

# Operador AND (e): Ambos precisam ser verdadeiros
# print(f'O cliente pode viajar? {tem_dinheiro and tem_tempo}.')
# print((f''))
# # Operador OR (ou): Pelo menos um tem que ser verdadeiro
# print(f'O cliente pode viajar? {tem_dinheiro or tem_tempo}.')
# # Operador NOT (não): Inverte o valor booleando
# print((f'O cliente pode viajar? {tem_dinheiro and not tem_tempo}.'))

# Manipulação  de Strings
# Define uma variável de tipo string
# frase = "  Aprender Pyhton é muito divertido!  "
# print(frase)
# # Concatenação
# nome = 'Maria'
# saudacao = 'Olá, ' + nome + "!"
# print(saudacao)
# # tamanho da string
# print(f'Tamanho da frase: {len(frase)}')
# # maiúsculas e minúsculas
# print(f'Maiúsculas: {frase.upper()}')
# print(f'Minúsculas: {frase.lower()}')
# # remover espaços em branco do ínicio e do fim
# frase_sem_espacos = frase.strip()
# print(f'Frase sem espaços:  "{frase_sem_espacos}"')
# # substituir texto
# print(f'Substituindo "divertido" por "legal": {frase_sem_espacos.replace("divertido", "legal")}')
# print(f'Tamanho da frase: {len(frase_sem_espacos)}')
# # fatiamento (slicing) - acessando partes de uma string
# # O índice em Python começa em 0
# print(frase_sem_espacos)
# print(f'O primeiro caracter é: {frase_sem_espacos[0]}')
# print(f'A palavra "Python": {frase_sem_espacos[9:15]}') # do índice 9 ao 14

# 7. ESTRUTURA DE DADOS - LISTAS
# Listas são coleções ordenadas de mutáveis de itens. Podem conter diferentes tipos de dados.
#criando uma lista
# frutas = ['maçã', 'banana', 'laranja', 'abacaxi']
# print(f'Lista de frutas: {frutas}')
# print(type(frutas))
# # acessando o ítem pelo índice
# print(f'A primeira fruta é: {frutas[0]}')
# print(f'A última fruta é: {frutas[-1]}')
# # adicionando um ítem ao final da lista
# frutas.append('uva')
# print(f'Lista após adicionar "uva": {frutas}')
# # removendo um ítem
# frutas.remove('laranja')
# print(frutas)
# # modificando um ítem
# frutas[0] = 'morango'
# print(frutas)
# # tamanho da lista
# print(f'A lista tem {len(frutas)} frutas')
# # deletando a lista
# del frutas
# print(frutas) # naõ aparece mais nada

# 7. ESTRUTURA DE DADOS - TUPLAS
# criando uma tupla
# coordenadas = (10.0, 20.5)
# print(f'Tupla de coordenadas: {coordenadas}')
# print(type(coordenadas))
# acessando o ítem pelo índice
# print(f'Coordenada x: {coordenadas[0]}')
# print(f'Coordenada y: {coordenadas[1]}')
# tentativa de modificar uma tupla resultará em erro (descomente para ver)
# coordenadas[0] = 15.0
# print(f'Coordenada x: {coordenadas[0]}')
# tuplas são úteis para dados que não devem ser alterados, como meses do ano, coordenadas, etc.
# dias_da_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
# print(dias_da_semana)
# print(f'o primeiro dia da semana: {dias_da_semana[0]}')

# 7. ESTRUTURA DE DADOS - DICIONÁRIO
# Dicionários são coleções de pares chaves: valor. São mutáveis
# criando um dicionário de informações de um aluno
# aluno = {
#     'nome': 'Bob',
#     'idade': 22,
#     'sexo': 'M',
#     'curso': 'Data Science Para Análise de Multivariada',
#     'aluno_ativo': True
# }
# print(f'Dicionario do aluno: {aluno}')
# # acessando um valor pela sua chave
# print(f'Dicionario do aluno: {aluno["nome"]}')
# print(f'Curso: {aluno.get('curso')}') # .get () é uma forma segura de acessar chaves
# # adicionando um novo para de chave-valor
# aluno['cidade'] = 'São Paulo'
# print(f'Dicionário atualizado:\n {aluno}')
# # modificando um valor existente
# aluno['idade'] = '23'
# print(f'Idade atualizada: {aluno["idade"]}')
# # removendo um par chave-valor
# del aluno["aluno_ativo"]
# print(f'Dicionario atualizado após remover a chave "ativo" :\n {aluno}')

# 7. ESTRUTURA DE DADOS - CONJUNTOS (sets)

# criando um conjunto (note que os ítens duplicados são removidos)
numeros = {1, 2, 3, 4 , 2, 3 ,5 }
# print(f'Conjunto de números (sem duplicatas): {numeros})')
# print(type(numeros))
# adicionando um ítem
# numeros.add(6)
# print(numeros)
# removendo um ítem
# numeros.remove(2)
# print(numeros)
# operações de conjuntos
# conjunto_a = {1, 2, 3, 4}
# conjunto_b = {3, 4, 5, 6}
# união dos conjuntos
# uniao = conjunto_a.union(conjunto_b)
# print(f'A união de A e B: {uniao}')
# interseção (elementos que estão em ambos conjuntos
# intersecao = conjunto_a.intersection(conjunto_b)
# print(f'Interseção de A e B: {intersecao}')

# CONVERSÃO ENTRE TIPOS DE DADOS (TYPE CASTING)
# É a conversão de um tipo de dado para outro
# convertendo de string para número integer
# numero_em_texto = '123'
# numero_inteiro = int(numero_em_texto)
# print(f'String "{numero_em_texto}" para inteiro: {numero_inteiro}, Tipo: {type(numero_inteiro)}')
# # convertendo de string para float
# numero_decimal_em_texto = '45.67'
# numero_float = float(numero_decimal_em_texto)
# print(f'String "{numero_decimal_em_texto}" para float: {numero_float}, Tipo: {type(numero_float)}')
# # convertendo de número para string
# idade = 25
# idade_texto = str(idade)
# print(f'Inteiro {idade} para String: "{idade_texto}", Tipo: {type(idade_texto)}')
# # convertendo entre estrutura de dados
# lista_com_duplicatas = [1,2,2,3,4,4,4,5]
# conjunto_unico = set(lista_com_duplicatas)
# lista_sem_duplicatas = list(conjunto_unico)
# print(f'\nLista original: {lista_com_duplicatas}')
# print(f'\nLista convertida para conjunto (remove duplicatas): {conjunto_unico}')
# print(f'\nLista convertida de volta para lista: {lista_sem_duplicatas}\n')

# ENTRADA E SAÍDA PADRÃO
# A forma mais comum de interagir com o usuário é através da entrada 'input' de dados pelo teclado
# e da saída 'output' de informações na tela

#SAÍDA DE DADOS COM PRINT()
# variáveis
# nome = 'juliana'
# idade = 28
# cidade = 'Rio de Janeiro'
# # usando f-strings (a forma mais moderna e recomendada)
# print(f'Olá, meu nome é {nome}, tenho {idade} anos e moro no {cidade}.')
# # formatando números
# preco = 49.95678
# print(f'O preço do produto é R$ {preco:.2f}') # formata para 2 casas decimais

# ENTRADA DE DADOS COM INPUT()
# a função input() sempre retorna uma string. Por isso é comum precisar fazer o type casting
# pedindo o nome do usuário (string)
nome_usuario = input('Qual é seu nome? ')
# pedindo a idade do usuário (precisa converter para int)
idade_usuario = int(input('Qual é sua idade? '))
# pedindo a cidade do usuário (string)
cidade_usuario = (input('Onde você mora? '))
from datetime import date
# pega o ano corrente na data definida no sistema operacionald sua máquina
ano_atual = date.today().year
# processando os dados
ano_nascimento = ano_atual - idade_usuario
# exibindo o resultado
print(f'\nOlá, {nome_usuario}! Bem vindo(a).')
print(f'Você tem {idade_usuario} anos e nasceu em {ano_nascimento}.')














