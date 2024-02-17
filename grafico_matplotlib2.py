
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
#colocando titulo no gráfico, tamho do titulo e uma separação do titulo entre o gráfico
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



