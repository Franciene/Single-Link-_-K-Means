import singlelink as singlelink
import numpy as numpy
from matplotlib import pyplot
import pandas as pd
from sklearn.metrics import adjusted_rand_score 

def mainMonkey():
    path = "bases/monkey.txt"
    data = path
    dataset = pd.read_csv(path, sep = '\t')
    # print("Rodando")
    # singlelink.singleLinkClustering(5, 12, data, "monkey")

    pyplot.scatter(dataset['D1'].values, dataset['D2'].values) 
    pyplot.savefig(f'grafico_geral_monkey.jpg')

    file = open('clusterFiles/singleLink/Resultado_monkey.txt', 'w')

    for i in range(5, 13):
        datasetRead = pd.read_csv(f'clusterFiles/SingleLink/monkey/monkey{i}.clu', sep = '\t', names=["sample_label", "class"])
        resultRead = pd.read_csv(f'clusterFiles/SingleLink/monkeyReal.clu', sep = '\t', names=["sample_label", "class"])

        x = datasetRead['class'].values
        y = resultRead['class'].values

        # print(adjusted_rand_score(x,y))

        rand = adjusted_rand_score(x,y)

        file.write("Indice Rand - " + ' ' + "monkey" + str(i) + ' = ' + str(round(rand, 3)) + '\n')

        # print(datasetRead['class'].values)

        pyplot.scatter(dataset['D1'].values, dataset['D2'].values, c = datasetRead['class'].values) 
        pyplot.savefig(f'grafico_monkey_{i}.jpg')

mainMonkey()
