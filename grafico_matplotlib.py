
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\luiz9\OneDrive\Documentos\criação de gráficos com o Matplotlib\curso-matplotlib\monitoramento_tempo.csv')

df.head()

df.info()

#convertendo a coluna para formato de data 
df['data'] = pd.to_datetime(df['data'])

df.info()

# passo 1 iniciando um gráfico simples ---------------------------------------------

#criando grafico passando df['data'] par o eixo x, e df['temperatura'] eixo y
plt.plot(df['data'], df['temperatura'])


# apasso 2 -----------------------------------------------------------------------

plt.plot(figsize=(15,8)) # passando o tamanho do grafico
plt.plot(df['data'], df['temperatura']) # eixo x df['data'], eixo y df['temperatura']
plt.title('Temperatura no Tempo') # passando um titulo para o gráfico 


# passo 3 -----------------------------------------------------------------------

#esta criando uma nova figura passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(df['data'], df['temperatura'])
eixo.set_title('temperatura no momento') # colocando um titulo no grafico

# passo 4 -----------------------------------------------------------------------

#esta criando uma nova figura dentro de uma variavel, passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(df['data'], df['temperatura'])
# colocando um titulo no grafico, e passando o tamanho da fonte
eixo.set_title('temperatura no momento', fontsize=25)
# colocando um titulo no eixo y, e passando o tamanho da fonte do eixo
eixo.set_ylabel('Temperatura', fontsize= 20)
# colocando um titulo no eixo x, e passando o tamanho da fonte do eixo
eixo.set_xlabel('Data', fontsize=20)

# passo 5 criando uma legenda e trocando cor do gráfico -------------------------------

#esta criando uma nova figura dentro de uma variavel, passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(df['data'], df['temperatura'], color = 'cadetblue') # colocando cor no gráfico
# colocando um titulo no grafico, e passando o tamanho da fonte
eixo.set_title('temperatura no momento', fontsize=25)
# colocando um titulo no eixo y, e passando o tamanho da fonte do eixo
eixo.set_ylabel('Temperatura', fontsize= 20)
# colocando um titulo no eixo x, e passando o tamanho da fonte do eixo
eixo.set_xlabel('Data', fontsize=20)
# criando uma legenda
eixo.legend(['temperatura'], loc = 'lower right', fontsize=15)#loc colocando o local da legenda


























