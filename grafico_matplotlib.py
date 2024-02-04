# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:34:44 2024

@author: luiz9
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\luiz9\OneDrive\Documentos\Data Visualization criação de gráficos com o Matplotlib\curso-matplotlib\monitoramento_tempo.csv')

df.head()

df.info()

#convertendo a coluna para formato de data 
df['data'] = pd.to_datetime(df['data'])

df.info()

#criando grafico passando df['data'] par o eixo x, e df['temperatura'] eixo y
plt.plot(df['data'], df['temperatura'])


plt.plot(figsize=(15,8)) # passando o tamanho do grafico
plt.plot(df['data'], df['temperatura']) # eixo x df['data'], eixo y df['temperatura']
plt.title('Temperatura no Tempo') # passando um titulo para o gráfico 

















