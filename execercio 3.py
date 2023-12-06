import numpy as np
# Criação de listas vazias para armazenar dados
nomes = []#Criando uma variável do tipo Lista vazia para receber os dados de nomes
idades = []
alturas = []
pesos = []

# Abrir e ler o arquivo CSV
with open('C:/Users/senai/Downloads/dados1.csv', 'r', encoding = 'ISO-8859-1') as batata:#
    lines = batata.readlines()


    for line in lines[1:]:  # Ignorar o cabeçalho
        nome, idade, altura, peso = line.strip().split(',')
        nomes.append(nome)
        idades.append(int(idade))
        alturas.append(int(altura))
        pesos.append(float(peso))

print(nomes)
print(idades)
print(alturas)
print(pesos)

# criando a variavel do array
nomes_nd = np.array(nomes)
idades_nd = np.array(idades)
alturas_nd = np.array(alturas)
pesos_nd = np.array(pesos)
media_idades = np.mean(idades)

print(f'{media_idades:.2f}')

# altura_maxima = np.max(alturas)
# pessoas_190 = np.count_nonzero(alturas == altura_maxima)
# # traz o indice de cada altura maxima
# pessoas_191 = np.argwhere(alturas == altura_maxima)
# # traz a quantidade de pessoas com altura maxima,obs(cria uma lista dentro de outra lista
# pessoas_192 = np.where(alturas == altura_maxima)
# # cria uma lista unica
# print(altura_maxima)
# print(pessoas_190)
# print(np.array(nomes)[pessoas_191])
# print(np.array(nomes)[pessoas_192])

# # pessoas acima de 70kg
# pessoas_70kg = np.count_nonzero(np.array(pesos) > 70)
# print(pessoas_70kg)
#
# # desvio padrao da idade
# desvio_idades = np.std(np.array(idades))
# print(f'{desvio_idades:.2f}')
#
# # pessoa mais velha
# maior_idade = np.max(idades)
# pessoas_65 = np.where(idades == maior_idade)
# print(maior_idade)
# # chamando um variavel
# print(nomes_nd[pessoas_65])
# print(len(nomes_nd[pessoas_65]))

# # passa primeiro o indice depois o tratamento // saber o imc
# imc_nd = np.array([(pesos[i]) / ((alturas[i]/100)**2) for i in range(len(pesos))])
# print(imc_nd)
# print(imc_nd.mean())

# # diferenca de idade
# diferencia_idade = idades_nd.max() - idades_nd.min()
# # para saber o maior e menor numero da lista
# diferencia_idade1 = np.ptp(idades)
# print(f'diferencia da idade do mais velho para o mais novo é {diferencia_idade}')
# print(diferencia_idade1)

# altura_media_25_30_1 = np.array([alturas for x in idades if x > 24 and x < 31])
# altura_media_25_30 = np.array([x for x in idades if x > 24 and x < 31])
# print(altura_media_25_30)
# print(altura_media_25_30_1)


# Quantas pessoas têm IMC acima de 25 (indicando sobrepeso)?

# sobrepeso = np.array([i for i in imc_nd if i > 25])
# sobrepeso_imc = np.count_nonzero(imc_nd >= 25)
# sobre = np.where(imc_nd >= 25)
# print(sobrepeso)
# print(sobrepeso_imc)
# print(len(nomes_nd[sobre]))

pessoas_170 = np.where(alturas_nd > 170)
print(nomes_nd[pessoas_170])

pessoas_70 = np.array([idades for x in pesos if x < 70])
print(pessoas_70.mean())

pesos_menor_70 = np.where(pesos_nd < 70)
print((idades_nd[pesos_menor_70]).mean())

