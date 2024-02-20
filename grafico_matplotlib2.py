
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv(r'C:\Users\luiz9\OneDrive\Documentos\criação de gráficos com o Matplotlib\curso-matplotlib\iris.csv')

df.head()


# criando gráfico de dispersão

'''
for i in df:
    print(i)
'''


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

#criando o grafico de dispesão colocando df['comprimento_sépala'] no eixo x
# e colocando df['largura_sépala'] no eixo y
eixo.scatter(df['comprimento_sépala'], df['largura_sépala'])
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
#criando titulo no eixo x e colocanto tamanha da fonta no titulo
eixo.set_xlabel('Comprimento_sépala', fontsize=15)
#criando titulo no eixo y e colocanto tamanha da fonta no titulo
eixo.set_ylabel('Largura_sépala', fontsize=15)


# 1 almentado o tamanho dos números do eixo -----------------------------------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

#criando o grafico de dispesão colocando df['comprimento_sépala'] no eixo x
# e colocando df['largura_sépala'] no eixo y
eixo.scatter(df['comprimento_sépala'], df['largura_sépala'])
#colocando titulo no gráfico, tamho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
#criando titulo no eixo x e colocanto tamanha da fonta no titulo
eixo.set_xlabel('Comprimento_sépala', fontsize=15)
#criando titulo no eixo y e colocanto tamanha da fonta no titulo
eixo.set_ylabel('Largura_sépala', fontsize=15)
#aumentando o tamanho da medida do eixo
eixo.tick_params(labelsize=15)


# 2 colocando uma cor para cada especie -------------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

cores = {'Iris-setosa' : 'r', 'Iris-versicolor' : 'b', 'Iris-virginica' : 'g'}

for especie in df['espécie'].unique():
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'],
                 color=cores[especie])


#colocando titulo no gráfico, tamho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
#criando titulo no eixo x e colocanto tamanha da fonta no titulo
eixo.set_xlabel('Comprimento_sépala', fontsize=15)
#criando titulo no eixo y e colocanto tamanha da fonta no titulo
eixo.set_ylabel('Largura_sépala', fontsize=15)
#aumentando o tamanho da medida do eixo
eixo.tick_params(labelsize=15)
#cirando uma legenda 
eixo.legend(cores, fontsize=20)



# 3 criando marcadores para cada especie -------------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

cores = {'Iris-setosa' : 'r', 'Iris-versicolor' : 'b', 'Iris-virginica' : 'g'}
marcadores = {'Iris-setosa' : 'x', 'Iris-versicolor' : 'o', 'Iris-virginica' : 'v'}

for especie in df['espécie'].unique():
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'],
                 color=cores[especie], marker=marcadores[especie])#colocando marcadores


#colocando titulo no gráfico, tamho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
#criando titulo no eixo x e colocanto tamanha da fonta no titulo
eixo.set_xlabel('Comprimento_sépala', fontsize=15)
#criando titulo no eixo y e colocanto tamanha da fonta no titulo
eixo.set_ylabel('Largura_sépala', fontsize=15)
#aumentando o tamanho da medida do eixo
eixo.tick_params(labelsize=15)
#cirando uma legenda 
eixo.legend(cores, fontsize=20)


# 3 aumentando o tamanho dos marcadores -------------------------------


fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

cores = {'Iris-setosa' : 'r', 'Iris-versicolor' : 'b', 'Iris-virginica' : 'g'}
marcadores = {'Iris-setosa' : 'x', 'Iris-versicolor' : 'o', 'Iris-virginica' : 'v'}

for especie in df['espécie'].unique():
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'],
                 color=cores[especie], marker=marcadores[especie],
                 s=100)#aumentando o tamanho dos marcadores


#colocando titulo no gráfico, tamho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de dispersão', fontsize=25, pad=15)
#criando titulo no eixo x e colocanto tamanha da fonta no titulo
eixo.set_xlabel('Comprimento_sépala', fontsize=15)
#criando titulo no eixo y e colocanto tamanha da fonta no titulo
eixo.set_ylabel('Largura_sépala', fontsize=15)
#aumentando o tamanho da medida do eixo
eixo.tick_params(labelsize=15)
#cirando uma legenda 
eixo.legend(cores, fontsize=20)


# 01 criando grafico de caixa   -------------------------------


#tamanho do grafico
fig = plt.figure(figsize=(5,4))

eixo = fig.add_axes([0, 0, 1, 1])


#criando grafico de 
eixo.boxplot(df['largura_pétala'])
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)

eixo.set_xticklabels(['largura_pétala'])



#--------------------------------------------------------------------------------
# 02 criando grafico de caixa para cada coluna comprimento_sépala
#largura_sépala, comprimento_pétala, largura_pétala -------------------------------


#tamanho do grafico
fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])


#criando grafico de 
eixo.boxplot(df.drop('espécie', axis=1).values,patch_artist=True)#preencher a caixa do grafico
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)

eixo.set_xticklabels(df.drop('espécie', axis=1).columns)



# 03 colocando cores diferente para cada caixo do gráfico


#tamanho do grafico
fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

cores = ['red', 'blue', 'orange', 'green']

#criando grafico de 
caixas = eixo.boxplot(df.drop('espécie', axis=1).values,patch_artist=True)#preencher a caixa do grafico
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)

eixo.set_xticklabels(df.drop('espécie', axis=1).columns)

#colocando cor nas caixas
for caixa, cor in zip(caixas['boxes'], cores):
    caixa.set(color=cor)


# 03 colocando marcadores no gráfico ----------------------------------------


#tamanho do grafico
fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0, 0, 1, 1])

cores = ['red', 'blue', 'orange', 'green']

#criando grafico de 
caixas = eixo.boxplot(df.drop('espécie', axis=1).values,patch_artist=True)#preencher a caixa do grafico
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)

eixo.set_xticklabels(df.drop('espécie', axis=1).columns)

#colocando cor nas caixas
for caixa, cor in zip(caixas['boxes'], cores):
    caixa.set(color=cor)


#colocando marcador no grafico
for outlier in caixas['fliers']:
    outlier.set(marker='x', markersize=8)#colocando tamanho do marcador



# 01 Criando gráfico de Histograma ----------------------------------------


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
#criando grafico histograma
eixo.hist(df['comprimento_pétala'])
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Histograma', fontsize=15, pad=10)
# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
# colocando grade dentro do gráfico
eixo.grid(True)



# 02 aumentando a quantidade de barras  ----------------------------------------
#Isso permite uma visualização mais detalhada da distribuição dos dados

fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
#criando grafico histograma
eixo.hist(df['comprimento_pétala'], bins=20)#colocando numero de barras no gráfico
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Histograma', fontsize=15, pad=10)
# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
# colocando grade dentro do gráfico
eixo.grid(True)


# 03 trocando a posição do gráfico -------------------------------------------


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
#criando grafico histograma, colocando numero de barras no gráfico
eixo.hist(df['comprimento_pétala'], bins=20, orientation='horizontal')#trocando a posição do gráfico
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Histograma', fontsize=15, pad=10)
# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
# colocando grade dentro do gráfico
eixo.grid(True)


# 03 colocando density=True no gráfico ------------------------------------


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
#criando grafico histograma, colocando numero de barras no gráfico
eixo.hist(df['comprimento_pétala'], bins=20, density=True)#trocando a posição do gráfico
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Histograma', fontsize=15, pad=10)
# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
# colocando grade dentro do gráfico
eixo.grid(True)


# 04 colocando a média e o desvio padrão ------------------------------------


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

#criando a média e o desvio padrão
mu, sigma = df['comprimento_sépala'].mean(), df['comprimento_sépala'].std()

#criando grafico histograma, colocando numero de barras no gráfico
eixo.hist(df['comprimento_pétala'], bins=20)
#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Histograma', fontsize=15, pad=10)
# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
# colocando grade dentro do gráfico
eixo.grid(True)

#colocando anotção no gráfico
eixo.annotate('$mu = {0:.2f}$\n$sigma = {1:.2f}$'.format(mu, sigma),
              xy=(4.5, 20), fontsize=20)#colocando localização e tamanho da fonte


# 05  ------------------------------------


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])

#criando a média e o desvio padrão
mu, sigma = df['comprimento_pétala'].mean(), df['comprimento_pétala'].std()

#criando grafico histograma, colocando numero de barras no gráfico
eixo.hist(df['comprimento_pétala'], bins=20)

#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Histograma', fontsize=15, pad=10)

# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)

# colocando grade dentro do gráfico
eixo.grid(True)

#colocando anotação no gráfico
eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
               xy=(4.5, 20), fontsize=20)

eixo.axvline(mu, color = 'k', linestyle='--')
eixo.annotate('média', xy=(mu-1.3, 28), fontsize=20)

eixo.axvline(df['comprimento_pétala'].median(), color='g', linestyle='--')
eixo.annotate('mediana', xy=(df['comprimento_pétala'].median(), 31), fontsize=20)



# 06 gráfico so da Iris-versicolor  ------------------------------------



fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])


df_iv = df[df['espécie'] == 'Iris-versicolor']


#criando a média e o desvio padrão
mu, sigma = df_iv['comprimento_pétala'].mean(), df_iv['comprimento_pétala'].std()

#criando grafico histograma, colocando numero de barras no gráfico
eixo.hist(df_iv['comprimento_pétala'], bins=20)

#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Iris-versicolor', fontsize=15, pad=10)

# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)

# colocando grade dentro do gráfico
eixo.grid(True)

#colocando anotação no gráfico
eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
               xy=(4.6, 6), fontsize=20)

eixo.axvline(mu, color = 'k', linestyle='--')
eixo.annotate('média', xy=(mu-0.5, 5.5), fontsize=20)

eixo.axvline(df_iv['comprimento_pétala'].median(), color='g', linestyle='--')
eixo.annotate('mediana', xy=(df_iv['comprimento_pétala'].median()-0.7, 6.5),
              fontsize=20, color='g')


#salvado imagem
fig.savefig('Histograma_iv.png', bbox_inches='tight')


# 07 gráfico so da Iris-setosa  ------------------------------------


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])


df_is = df[df['espécie'] == 'Iris-setosa']


#criando a média e o desvio padrão
mu, sigma = df_is['comprimento_pétala'].mean(), df_is['comprimento_pétala'].std()

#criando grafico histograma, colocando numero de barras no gráfico
eixo.hist(df_is['comprimento_pétala'], bins=20)

#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Iris-setosa', fontsize=15, pad=10)

# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)

# colocando grade dentro do gráfico
eixo.grid(True)

#colocando anotação no gráfico
eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
               xy=(1.7, 7), fontsize=20)

eixo.axvline(mu, color = 'k', linestyle='--')
eixo.annotate('média', xy=(mu-0.2, 13.5), fontsize=20)

eixo.axvline(df_is['comprimento_pétala'].median(), color='g', linestyle='--')
eixo.annotate('mediana', xy=(df_is['comprimento_pétala'].median()+0.05, 12),
              fontsize=20, color='g')


#salvado imagem
fig.savefig('Histograma_is.png', bbox_inches='tight')



# 07 gráfico so da Iris-virginica  ------------------------------------


fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])


df_ivc = df[df['espécie'] == 'Iris-virginica']


#criando a média e o desvio padrão
mu, sigma = df_ivc['comprimento_pétala'].mean(), df_ivc['comprimento_pétala'].std()

#criando grafico histograma, colocando numero de barras no gráfico
eixo.hist(df_ivc['comprimento_pétala'], bins=20)

#colocando titulo no gráfico, tamanho do titulo e uma separação do titulo entre o gráfico
eixo.set_title('Iris-virginica', fontsize=15, pad=10)

# colocando titulo no eixo x tamanho de fonte
eixo.set_xlabel('Comprimento da pétala', fontsize=15)

# colocando grade dentro do gráfico
eixo.grid(True)

#colocando anotação no gráfico
eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
               xy=(6.3, 7), fontsize=20)

eixo.axvline(mu, color = 'k', linestyle='--')
eixo.annotate('média', xy=(mu, 8), fontsize=20)

eixo.axvline(df_ivc['comprimento_pétala'].median(), color='g', linestyle='--')
eixo.annotate('mediana', xy=(df_ivc['comprimento_pétala'].median(), 7),
              fontsize=20, color='g')


#salvado imagem
fig.savefig('Histograma_ivc.png', bbox_inches='tight')



# 08 combinando as três imagem ------------------------------------

largura, altura = Image.open('Histograma_ivc.png').size

combinada = Image.new("RGB", (3*largura, altura))


intervalo = 0

for imagem in map(Image.open, ['Histograma_iv.png', 'Histograma_is.png',
                              'Histograma_ivc.png']):
    combinada.paste(imagem, (intervalo, 0))
    intervalo += largura
    
    
combinada.save('combinada.png')


'''

for i in df['espécie'].unique():
    print(i)



for i in df:
    print(i)

'''
