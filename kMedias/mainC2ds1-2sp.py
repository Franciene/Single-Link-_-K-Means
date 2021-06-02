import clustering as clustering
import numpy as numpy
from sklearn.metrics import adjusted_rand_score 
from matplotlib import pyplot
import pandas as pd
from sklearn.metrics import adjusted_rand_score 


def main():
    path = "bases/c2ds1-2sp.txt"
    data = path

    # nClusters = int(input("Quantos clusters voce deseja utilizar?\n"))
    # nIterations = int(input("Quantas iteracoes voce deseja realizar?\n"))
    
    clustering.kMeans(2, 5, data, "c2ds1-2sp")

    dataset = pd.read_csv(f'bases/c2ds1-2sp.txt', sep = '\t')
    datasetRead = pd.read_csv(f'generated/c2ds1-2sp.clu', sep = '\t', names=["sample_label", "class"])

    pyplot.scatter(dataset['d1'].values, dataset['d2'].values, c = datasetRead['class'].values) 
    pyplot.savefig(f'grafico_c2ds1-2sp_C2.jpg')

    pyplot.scatter(dataset['d1'].values, dataset['d2'].values) 
    pyplot.savefig(f'grafico_geral_c2ds1-2sp.jpg')

    resultRead = pd.read_csv(f'generated/c2ds1-2spReal.clu', sep = '\t', names=["sample_label", "class"])

    file = open('generated/Resultado_c2ds1-2sp.txt', 'w')

    x = datasetRead['class'].values
    y = resultRead['class'].values

    rand = adjusted_rand_score(x,y)
    file.write("Indice Rand - " + ' ' + "c2ds1-2sp" + ' = ' + str(round(rand, 3)) + '\n')

main()
