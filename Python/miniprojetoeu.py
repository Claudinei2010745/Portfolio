# 1. Definição do Problema de Negócio
# 1.1. O Problema de Negócio
#
'''Nossa loja de e-commerce está em fase de crescimento, registrando um volume cada vez maior de
# transações diárias. No entanto, essa grande quantidade de dados de vendas, em seu estado bruto,
# é como um baú de tesouro trancado: sabemos que há valor ali, mas não conseguimos acessá-lo.
# Atualmente, muitas de nossas decisões estratégicas são baseadas em intuição e observações parciais, o que nos leva a enfrentar os seguintes desafios:
# Gestão de Estoque Ineficiente: Não temos clareza sobre quais produtos são nossos "campeões de venda"
# e quais estão parados nas prateleiras. Isso resulta em excesso de estoque de itens de baixa procura e
# falta de produtos de alta demanda.Marketing com Baixo Retorno: Nossas campanhas de marketing
# são genéricas, pois não sabemos quais categorias de produtos atraem mais os clientes ou em quais
# regiões geográficas nosso público está mais concentrado.
# Perda de Oportunidades Sazonais: Não conseguimos identificar padrões ou tendências de vendas ao
# longo dos meses. Isso nos impede de planejar promoções estratégicas para períodos de alta ou de
# criar ações para impulsionar as vendas em meses de baixa.
# Expansão sem Direção: Temos o desejo de expandir, mas não sabemos quais mercados regionais são mais
# promissores ou onde nossos esforços logísticos deveriam ser focados.
O problema central é a falta de visibilidade clara sobre a performance do negócio, o que nos impede de
tomar decisões rápidas, inteligentes e baseadas em evidências.
1.2. Objetivos do Projeto
Este projeto de análise de dados visa transformar nossos dados brutos de vendas em insights acionáveis.
O objetivo é responder a quatro perguntas de negócio fundamentais:
O que vender? Identificar os produtos de maior sucesso para otimizar nosso portfólio e estoque.
Onde focar? Compreender quais categorias de produtos geram a maior parte da nossa receita.
Quando agir? Analisar a performance de vendas ao longo do tempo para identificar tendências, picos e
sazonalidades.
Para onde expandir? Mapear a distribuição geográfica de nossas vendas para descobrir nossos mercados mais fortes.
1.3. Solução Proposta
A solução consiste em consolidar, limpar e analisar o histórico de dados de vendas da nossa plataforma.
Utilizando ferramentas de análise de dados (como Python com Pandas, NumPy e Matplotlib), vamos processar e
ssas informações e criar um relatório visual que apresente as descobertas de forma clara e intuitiva para as
equipes de gestão, marketing e operações.
1.4. Resultados Esperados e Benefícios de Negócio
Ao final deste projeto, esperamos alcançar os seguintes resultados:
Otimização de Estoque: Com a lista dos produtos mais e menos vendidos, poderemos ajustar nossas
compras, reduzir custos com armazenamento e evitar a perda de vendas por falta de produto.
Marketing Direcionado e Eficaz: Sabendo quais categorias e regiões são mais lucrativas, a equipe de
marketing poderá criar campanhas segmentadas, aumentando o retorno sobre o investimento (ROI).
Planejamento Estratégico: A visualização das tendências mensais permitirá um melhor planejamento financeiro,
 promocional e de recursos, antecipando períodos de alta e baixa demanda.
Decisões Baseadas em Dados: Substituiremos a intuição por dados concretos, criando uma cultura orientada a
dados que impulsionará o crescimento sustentável do negócio.'''
import matplotlib
# IMPORTANÇÃO DAS BIBLIOTECAS
import watermark # marcas de água
import pandas as pd # manipulação de dados em tabelas
import numpy as np # operações matemáticas e arrays
import matplotlib.pyplot as plt # geração de gráficos
import seaborn as sns # visualização estatísticas de dados
import random # geração de números aleatórios
from datetime import datetime, timedelta # manipulação de datas e intervalos de tempo

from IPython.core.pylabtools import figsize

print(watermark.__version__)
print(pd.__version__)
print(matplotlib.__version__)
print(sns.__version__)
print(np.__version__)

# . FUNÇÃO PARA DADOS FICTÍCIOS
# definição da função para gerar dados fictícios de vendas
def dsa_gera_dados_ficticios(num_registros=600):
    '''Gera um dataframe do pandas com dados de vendas fictícias.'''
    # mensagem inicial indicando a quantidade de registros a serem gerados
    print(f'Iniciando a geração de {num_registros} registros de vendas...')
    # dicionário com produtos, suas categorias e preços
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00},
    }
    # cria uma lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())
    # dicionário com cidades e os seus respectivos estados
    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }
    # Cria uma lista com apenas nomes das cidades
    lista_cidades = list(cidades_estados.keys())
    # lista que armazenará os registros de vendas
    dados_vendas = []
    # define a data inicial dos pedidos
    data_inicial = datetime(2026, 1, 1)
    # loop para gerar os registros de vendas
    for i in range(num_registros):
        # seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)
        # seleciona aleatoriamente uma cidade
        cidade = random.choice(lista_cidades)
        # gera uma quantidade vendida entre 1 e 7
        quantidade = np.random.randint(1, 8)
        # calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i / 5), hours=random.randint(0, 23))
        # se o produto for Mouse ou teclado, aplica desconto aleatório de 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']
        # adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade],
        })
    # Mensagem final indicando que a geração terminou
    print('Geração de dados concluída')
    # retorna os dados no formato de dataframe
    # pd.set_option('display.max_columns', None) retorna todas as colunas
    return pd.DataFrame(dados_vendas)
    print(pd.DataFrame(dados_vendas))

dsa_gera_dados_ficticios()

    # 4. GERAR, CARREGAR E EXPLORAR OS DADOS
    # gera os dados chamando a função da célula interior
df_vendas = dsa_gera_dados_ficticios(500)
# shape
print(df_vendas.shape)
# exibe as 5 primeiras linhas do dataframe
print(df_vendas.head())
# exibe as 5 últimas linhas do dataframe
print(df_vendas.tail())
# exibe as informações gerais sobre o dataframe (tipos de dados, valores não nulos)
print(df_vendas.info())
# resumo estatístico
print(df_vendas.describe())
# tipos de dados
print(df_vendas.dtypes)

# 5. LIMPEZA, PRÉ-PROCESSAMENTO E ENGENHARIA DE ATRIBUTOS
# Se a coluna 'Data_Pedido' não estiver como tipo datetime, precisamos fazer a conversão explícita
# A coluna pode ser usada para análise temporal
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])
# engenharia de atributos
# criando a coluna 'faturamento' (preco x quantidade)
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']
# engenharia de atributos
# usando uma função lambda para criar uma coluna de status de entrega
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG']
                                                        else 'Normal')
# exibe informações gerais sobre o dataframe (tipos de dados, valores não nulos)
print(df_vendas)
df_vendas.info()

# 6. ANÁLISE 1 - TOP 10 PRODUTOS MAIS VENDIDOS
# Agrupa por nome do produto, soma a quantidade e ordena para encontrar os mais vendidos
top_10_produtos = df_vendas.groupby('Nome_produto')['Quantidade'].sum().sort_values(ascending=False).head(10)
print(top_10_produtos)

# define um estilo para os gráficos
sns.set_style('whitegrid')
# cria a figura e os eixos
plt.figure(figsize=(8, 6))
# cria gráfico de barras horizontais
top_10_produtos.sort_values(ascending=True).plot(kind='barh', color='skyblue')
# adiciona títulos e labels
plt.title('Top 10 produtos Mais Vendidos', fontsize=16)
plt.xlabel('Quantidade Vendida', fontsize=12)
plt.ylabel('Produto', fontsize=12)
# exibe o gráfico
plt.tight_layout()
plt.show()

# 7. ANÁLISE 2 - FATURAMENTO MENSAL
# cria uma coluna 'Mês' para facilitar o agrupamento mensal
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')
# agrupa por mês e soma o faturamento
faturamento_mensal = df_vendas.groupby('Mes') ['Faturamento'].sum()
# converte o índice para string para facilitar a plotagem no gráfico
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')
# formata as duas casas decimais
faturamento_mensal.map('R$ {:,.2f}'.format)
# cria uma nova figura com tamanho de 12 por 6 polegadas
plt.figure(figsize=(12, 6))
# plota os dados de faturamento mensal em formato de linha
faturamento_mensal.plot(kind='line', marker='o', linestyle='-', color='green')
# define o título do gráfico com fonte de tamanho 16
plt.title('Evolução do Faturamento Mensal', fontsize=16)
# define o rótulo do eixo X
plt.xlabel('Mês', fontsize=12)
# define o rótulo do eixo Y
plt.ylabel('Faturamento (R$)', fontsize=12)
# rotaciona os valores do eixo x em 45 graus para melhor visualização
plt.xticks(rotation=45)
# adiciona uma grade com estilo tracejado e linhas finas
plt.grid(True, which='both', linestyle='--', linewidth='0.5')
# ajusta automaticamente os elementos para evitar sobreposição
plt.tight_layout()
# exibe o gráfico
plt.show()

# 8. Análise 3 - VENDAS POR ESTADO
# agrupa por estado e soma o faturamento
vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)
# formata para duas casas decimais
# vendas_estado = vendas_estado.map('R$ {:,.2f}'.format)
print(vendas_estado)
# cria uma nova figura com tamanho de 12 por 7 polegadas
plt.figure(figsize=(12, 7))
# plota os dados de faturamento por estado em formato de gráfico de barras
# usando a paleta de cores 'rocket' do seaborn
vendas_estado.plot(kind='bar', color=sns.color_palette('husl', 7))
# define o título do gráfico com fonte de tamanho 16
plt.title('Faturamento Por Estado', fontsize=16)
# define o rótulo do eixo X
plt.xlabel('Estado', fontsize=12)
# define o rótulo do eixo Y
plt.ylabel('Faturamento (R$)', fontsize=12)
# mantém os rótulos do eixo X na horizontal (sem rotação)
plt.xticks(rotation=0)
# adiciona uma grade com estilo tracejado e linhas finas
plt.tight_layout()
plt.show()

# 9. Análise 4 - faturamento por categoria
# agrupa por categoria, soma o faturamento e formata como moeda para melhor leitura
faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)
# o .map ('{:,.2f}'.format) é opcional, mas deixa a visualização do número mais clara
faturamento_categoria.map('R$ {:,.2f}'.format)
print(faturamento_categoria)
# importa a função funcformatter para formatar os eixos
from matplotlib.ticker import FuncFormatter
# ordena os dados para os gráficos ficarem mais fáceis de ler
faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)
# cria a figura e os eixos (ax) com plt.subplots()
# isso nos dá mais controle sobre os elementos do gráficos
fig, ax = plt.subplots(figsize=(12, 7))
# cria uma função para formatar os números
# esta função recebe um valor 'y' e o transforma numa string no formato 'R$ XX K'
def formatador_milhares(y, pos):
    '''Formata o valor em milhares (K) com o cifrão R$.'''
    return f'R$ {y/1000:,.0f}K'
# cria o objeto formatador
formatter = FuncFormatter(formatador_milhares)
# Aplica o formatador ao eixo Y (ax, yaxis)
ax.yaxis.set_major_formatter(formatter)
# plota os dados usando o objeto 'ax'
faturamento_ordenado.plot(kind='bar', ax = ax, color=sns.color_palette('viridis', len(faturamento_ordenado)))
# adiciona títulos e labels usando 'ax.set_...'
ax.set_title('Faturamento Por Categoria', fontsize=16)
ax.set_xlabel('Categoria', fontsize=12)
ax.set_ylabel('Faturamento', fontsize=12)
# ajusta a rotação dos rótulos do eixo X
plt.xticks(rotation=45, ha='right')
# garante que tudo fique bem ajustado na imagem final
plt.tight_layout()
# exibe o gráfico
plt.show()







