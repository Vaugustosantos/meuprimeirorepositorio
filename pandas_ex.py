import pandas as pd
import numpy as np
import random as rd

data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
        'Idade': [25, 32, 30, 28, 45],
        'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Dentista']}
df = pd.DataFrame(data)

# loc -> traz o valor que esta dentro da posicao
df.loc[df['Nome'] == 'Ana',['Profissão']] = 'Engenheira'
#print(df)

df_idade = df.sort_values(by='Idade', ascending=False)
#print(df_idade)

# fillna -> vou esta preenchendo vazio
df['Salário'] = df.fillna(value=0, inplace=True)
# df.loc[df['Nome'] == 'João', ['Salário']] = 5000
# df.loc[df['Nome'] == 'Pedro', ['Salário']] = 3500
# df.loc[df['Nome'] == 'Lucas', ['Salário']] = 8000
# print(df)

# sample -> traz uma lista com aleatorios comandos

var1 = df['Nome'].sample(3).index
for i in var1:
        df.loc[i, 'Salário'] = rd.randint(2000, 6000)
# print(df)

# print()
# fillna -> altera os campos que estao nulos
# df['Salário'] = df['Salário'].fillna(0)
# df = df['Salário'].mean().round(2)
# print(df)


# groupby -> Agrupe DataFrame usando um mapeador ou por uma série de colunas.
media = df.groupby('Profissão')['Idade'].mean()
# print(media)

data2 = {'Nome': ['Felipe', 'Isabel'],
         'Idade': [35, 40],
         'Profissão': ['Artista', 'Engenheira'],
         'Salário': [2500, 3500]}
data2 = pd.DataFrame(data2)

df3 = pd.concat([df, data2])

# print(df3)
print(len(df3['Nome']))
df3.index = range()


