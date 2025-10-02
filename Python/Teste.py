#%%
2 + 2

#%%
print('Olá Mundo!')
#%%
numeros = list(range(1, 101))
for numero in numeros:
    if numero % 2 == 0 and numero % 4 ==0:
        print(numero, end=' ')
#%%
numeros = list(range(1, 101))
#list comprehension para gerar uma lista somente com os números pares e devisíveis por 4
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
print(pares_div4, end=' ')
#%% md
        # PSEUDOCÓDIGO 1
# Exiba 'Bem vindo ao calculador de área do paralelogramo'
# Peça para o usuário inserir o comprimento da base
# Armazena o comprimento da base em uma variável
# Peça para o usuário inserir a altura
# Armazene a altura em uma variável
# Calcule a área do paralelogramo base*altura
# Armazene o resultado em uma variável
# Exiba o resultado

# Fim
#%% raw
print('Bem vindo ao calculador de área de paralelogramo')
#%%
base = float(input('Insira o comprimento da base: '))
#%%
altura = float(input('Insira a altura: '))
#%%
area = base * altura
#%%
print('A área do paralelogramo é: ', area)
#%% md
#       PSEUDOCÓDIGO 2 - Calculador Simples
# Inicie
#     Exiba 'Bem vindo a Calculadora'
#     Peça para o usuário inserir o primeiro número
#     Armazene o primeiro número em uma variável
#     Peça para o usuário inserir o segundo número
#     Armazene o segundo número em uma variável
#     Peça para o usuário selecionar uma operação (+, -, *, /)
#     Armazene a operação em uma variável
#     Utilize a operação selecionada e os números para realizar o cálculo
    



#%%
print('Bem vindo a Calculadora')
primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))   
operação = str(input('Qual operação deseja fazer: (+ - * /)\n'))
if operação == '+':
    print('Você escolheu SOMA') 
    operação = primeiro_numero + segundo_numero
elif operação == '-':
    print('Você escolheu SUBTRAÇÃO')
    operação = primeiro_numero - segundo_numero
elif operação == '*':
    print('Você escolheu MULTIPLICAÇÃO')
    operação = primeiro_numero * segundo_numero
elif operação == '/':
    operação = primeiro_numero / segundo_numero
    print('Você escolheu DIVISÃO')
else:
    print('Opção inválida!')
        
print('O resultado da operação é: ', operação)
print()
print('FIM!')
#%% md
#         Pseudocódigo 3 - Algoritmo Bubble Sort
# Bubble Sort é um algoritmo de ordenação simples que funciona comparando cada elemento com o próximo
# trocando-os de lugar se eles estiverem em ordem incorreta. O algoritmo repete esse processo até várias vezes até que todos
# os elementos estejam ordenados. A cada passagem, o maior elemento flutua para o final do array, como uma bolha, dando origem
# ao nome algoritmo.
#     Inicie
#         Para cada elemento i no array de tamanho n
#             Para cada elemento j no array de tamanho n - 1
#                 Se o elemento i for maior que elemento j
#                     Troque os elementos i e j
#         Exiba o array ordenado
#     Fim

#%%
lista = [1, 8, 7, 5, 2, 9, 4]
def bubble_sort(arr):
    n = len(arr)
    #para cada elemento do array
    for i in range(n):
        #for cada elemento j do array
        for j in range(0, n-i-1):
            #Se elemento i for maior que elemento j
            if arr[j] > arr[j + 1]:
                #Troque os elementos i e j
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble_sort(lista))
    

#%%
