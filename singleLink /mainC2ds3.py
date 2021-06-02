import singlelink as singlelink
import numpy as numpy
from matplotlib import pyplot
import pandas as pd
from sklearn.metrics import adjusted_rand_score 

def mainC2ds1():
    path = "bases/c2ds3-2g.txt"
    data = path
    dataset = pd.read_csv(path, sep = '\t')
    # print("Rodando")
    singlelink.singleLinkClustering(2, 5, data, "c2ds3-2g")

    pyplot.scatter(dataset['d1'].values, dataset['d2'].values) 
    pyplot.savefig(f'grafico_geral_c2ds3-2g.jpg')

    file = open('clusterFiles/singleLink/Resultado_c2ds3-2g.txt', 'w')

    for i in range(2, 6):
        datasetRead = pd.read_csv(f'clusterFiles/SingleLink/c2ds3-2g{i}.clu', sep = '\t', names=["sample_label", "class"])
        resultRead = pd.read_csv(f'clusterFiles/SingleLink/c2ds3-2gReal.clu', sep = '\t', names=["sample_label", "class"])

        x = datasetRead['class'].values
        y = resultRead['class'].values

        # print(adjusted_rand_score(x,y))

        rand = adjusted_rand_score(x,y)

        file.write("Indice Rand - " + ' ' + "c2ds3-2g" + str(i) + ' = ' + str(round(rand, 3)) + '\n')

        # print(datasetRead['class'].values)

        pyplot.scatter(dataset['d1'].values, dataset['d2'].values, c = datasetRead['class'].values) 
        pyplot.savefig(f'grafico_c2ds3-2g_{i}.jpg')

mainC2ds1()
