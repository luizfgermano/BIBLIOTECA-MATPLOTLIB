
import pandas as pd
import matplotlib.pyplot as plt
import datetime

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


# passo 6 mexendo no tamanho da linhas ----------------------------------------------------


#esta criando uma nova figura dentro de uma variavel, passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
# colocando cor no gráfico, e almentando o tamho da linha 
eixo.plot(df['data'], df['temperatura'], color = 'cadetblue', lw = 0.4)
# colocando um titulo no grafico, e passando o tamanho da fonte
eixo.set_title('temperatura no momento', fontsize=25)
# colocando um titulo no eixo y, e passando o tamanho da fonte do eixo
eixo.set_ylabel('Temperatura', fontsize= 20)
# colocando um titulo no eixo x, e passando o tamanho da fonte do eixo
eixo.set_xlabel('Data', fontsize=20)
# criando uma legenda
eixo.legend(['temperatura'], loc = 'lower right', fontsize=15)#loc colocando o local da legenda


# passo 6 mexendo no estilo da linhas ----------------------------------------------------

#esta criando uma nova figura dentro de uma variavel, passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
# colocando cor no gráfico, e almentando o tamho da linha 
eixo.plot(df['data'], df['temperatura'], color = 'cadetblue', ls = 'dotted')
# colocando um titulo no grafico, e passando o tamanho da fonte
eixo.set_title('temperatura no momento', fontsize=25)
# colocando um titulo no eixo y, e passando o tamanho da fonte do eixo
eixo.set_ylabel('Temperatura', fontsize= 20)
# colocando um titulo no eixo x, e passando o tamanho da fonte do eixo
eixo.set_xlabel('Data', fontsize=20)
# criando uma legenda
eixo.legend(['temperatura'], loc = 'lower right', fontsize=15)#loc colocando o local da legenda


# passo 7  incluindo data de inicio e data final do gráfico --------------------------


#esta criando uma nova figura dentro de uma variavel, passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
# colocando cor no gráfico, e almentando o tamho da linha 
eixo.plot(df['data'], df['temperatura'], color = 'cadetblue')
# passando o periodo do grafico inicio ate o final
eixo.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
# colocando um titulo no grafico, e passando o tamanho da fonte
eixo.set_title('temperatura no momento', fontsize=25)
# colocando um titulo no eixo y, e passando o tamanho da fonte do eixo
eixo.set_ylabel('Temperatura', fontsize= 20)
# colocando um titulo no eixo x, e passando o tamanho da fonte do eixo
eixo.set_xlabel('Data', fontsize=20)
# criando uma legenda
eixo.legend(['temperatura'], loc = 'lower right', fontsize=15)#loc colocando o local da legenda


# passo 8 adicionando marcadores --------------------------

#esta criando uma nova figura dentro de uma variavel, passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
# colocando cor no gráfico, criando marcador  
eixo.plot(df['data'], df['temperatura'], color = 'g', marker = 'o')
# passando o periodo do grafico inicio ate o final
eixo.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
# colocando um titulo no grafico, e passando o tamanho da fonte
eixo.set_title('temperatura no momento', fontsize=25)
# colocando um titulo no eixo y, e passando o tamanho da fonte do eixo
eixo.set_ylabel('Temperatura', fontsize= 20)
# colocando um titulo no eixo x, e passando o tamanho da fonte do eixo
eixo.set_xlabel('Data', fontsize=20)
# criando uma legenda
eixo.legend(['temperatura'], loc = 'lower right', fontsize=15)#loc colocando o local da legenda


# passo 9 colocando grade no gráfico--------------------------

#esta criando uma nova figura dentro de uma variavel, passando o tamanho 
fig = plt.figure(figsize=(15,8))
#fazendo um eixo para colocar o gráfico dentro
eixo = fig.add_axes([0, 0, 1, 1])
# colocando cor no gráfico, criando marcador  
eixo.plot(df['data'], df['temperatura'], color = 'cadetblue')
# passando o periodo do grafico inicio ate o final
eixo.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
# colocando um titulo no grafico, e passando o tamanho da fonte
eixo.set_title('temperatura no momento', fontsize=25)
# colocando um titulo no eixo y, e passando o tamanho da fonte do eixo
eixo.set_ylabel('Temperatura', fontsize= 20)
# colocando um titulo no eixo x, e passando o tamanho da fonte do eixo
eixo.set_xlabel('Data', fontsize=20)
# criando uma legenda
eixo.legend(['temperatura'], loc = 'lower right', fontsize=15)#loc colocando o local da legenda
# colocando grade no grafico
eixo.grid(True)


# passo 10 criando um novo gráfico com dois eixo -----------------------------------

fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.1, 0.5, 0.4, 0.4])


# passo 11 colocando informação nos dois eixo ---------------------------------

fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

eixo2 = fig.add_axes([0.1, 0.5, 0.4, 0.4])
#criando grafico passando df['data'] par o eixo x, e df['temperatura'] eixo y
eixo.plot(df['data'], df['temperatura'], color='red')
eixo.grid(True) # colocando grade no fundo do gráfico
#colocando titulo, e não deixando o titulo muito proximo
eixo.set_title('Temperatura no Momento', fontsize=25, pad=20)
eixo.legend(['temperatura'], loc='best', fontsize=15)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)

#criando gráfico no eixo 2
eixo2.plot(df['data'], df['temperatura'], color='blue')
eixo2.set_title('Temperatura no Momento', fontsize=15)
eixo2.legend(['temperatura'], loc='best', fontsize=8)
eixo2.set_ylabel('Temperatura', fontsize=10)
eixo2.set_xlabel('Data', fontsize=10)


# passo 12 mudando gráfoco dois de lugar ---------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3])

#criando grafico passando df['data'] par o eixo x, e df['temperatura'] eixo y
eixo.plot(df['data'], df['temperatura'], color='red')
#colocando um periodo no gráfico
eixo.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
eixo.grid(True) # colocando grade no fundo do gráfico
#colocando titulo, e não deixando o titulo muito proximo
eixo.set_title('Temperatura em 2014', fontsize=25, pad=20)
eixo.legend(['temperatura'], loc='lower right', fontsize=15)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)

#criando gráfico no eixo 2
eixo2.plot(df['data'], df['temperatura'], color='blue')
eixo2.set_title('Temperatura no Momento', fontsize=15)
eixo2.legend(['temperatura'], loc='best', fontsize=8)
eixo2.set_ylabel('Temperatura', fontsize=10)
eixo2.set_xlabel('Data', fontsize=10)
eixo2.grid(True)


# passo 13 trocando os periodos dos graficos ---------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3])

#criando grafico passando df['data'] par o eixo x, e df['temperatura'] eixo y
eixo.plot(df['data'], df['temperatura'], color='red')
#colocando um periodo no gráfico
eixo.set_xlim(datetime.datetime(2014,5,1), datetime.datetime(2014,6,1))
eixo.grid(True) # colocando grade no fundo do gráfico
#colocando titulo, e não deixando o titulo muito proximo
eixo.set_title('Temperatura em 2014', fontsize=25, pad=20)
eixo.legend(['temperatura'], loc='lower right', fontsize=15)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)

#criando gráfico no eixo 2
eixo2.plot(df['data'], df['temperatura'], color='blue')
eixo2.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
eixo2.set_title('Temperatura no Momento', fontsize=15)
eixo2.legend(['temperatura'], loc='best', fontsize=8)
eixo2.set_ylabel('Temperatura', fontsize=10)
eixo2.set_xlabel('Data', fontsize=10)
eixo2.grid(True)


# passo 13  dando limite para o eixo y---------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3])

#criando grafico passando df['data'] par o eixo x, e df['temperatura'] eixo y
eixo.plot(df['data'], df['temperatura'], color='red')
#colocando um periodo no gráfico
eixo.set_xlim(datetime.datetime(2014,5,1), datetime.datetime(2014,6,1))
eixo.set_ylim(270, 320) #dando limite para o eixo y
eixo.grid(True) # colocando grade no fundo do gráfico
#colocando titulo, e não deixando o titulo muito proximo
eixo.set_title('Temperatura em maio 2014', fontsize=25, pad=20)
eixo.legend(['temperatura'], loc='lower right', fontsize=15)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)

#criando gráfico no eixo 2
eixo2.plot(df['data'], df['temperatura'], color='blue')
eixo2.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
eixo2.set_title('Temperatura no ano 2014', fontsize=15)
eixo2.legend(['temperatura'], loc='best', fontsize=8)
eixo2.set_ylabel('Temperatura', fontsize=10)
eixo2.set_xlabel('Data', fontsize=10)
eixo2.grid(True)


# passo 14 ---------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3])

#criando grafico passando df['data'] par o eixo x, e df['temperatura'] eixo y
eixo.plot(df['data'], df['temperatura'], color='g')
#colocando um periodo no gráfico
eixo.set_xlim(datetime.datetime(2014,5,1), datetime.datetime(2014,6,1))
eixo.set_ylim(270, 320) #dando limite para o eixo y
eixo.grid(True) # colocando grade no fundo do gráfico
#colocando titulo, e não deixando o titulo muito proximo
eixo.set_title('Temperatura em maio 2014', fontsize=25, pad=20)
eixo.legend(['temperatura'], loc='lower right', fontsize=15)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)

azul_esquerda = df['data'] < datetime.datetime(2014, 5, 1)
azul_direita = df['data'] > datetime.datetime(2014, 6, 1)

#criando gráfico no eixo 2
eixo2.plot(df['data'], df['temperatura'], color='g')
eixo2.plot(df[azul_esquerda]['data'], df[azul_esquerda]['temperatura'], color='b')
eixo2.plot(df[azul_direita]['data'], df[azul_direita]['temperatura'], color='b')
eixo2.set_xlim(datetime.datetime(2014,1,1), datetime.datetime(2015,1,1))
eixo2.set_title('Temperatura no ano 2014', fontsize=15)
eixo2.legend(['temperatura'], loc='best', fontsize=8)
eixo2.set_ylabel('Temperatura', fontsize=10)
eixo2.set_xlabel('Data', fontsize=10)
eixo2.grid(True)




























