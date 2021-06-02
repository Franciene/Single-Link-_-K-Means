import clustering as clustering
import numpy as numpy
from sklearn.metrics import adjusted_rand_score 
from matplotlib import pyplot
import pandas as pd
from sklearn.metrics import adjusted_rand_score 


def main():
    path = "bases/monkey.txt"
    data = path

    # nClusters = int(input("Quantos clusters voce deseja utilizar?\n"))
    # nIterations = int(input("Quantas iteracoes voce deseja realizar?\n"))
    
    clustering.kMeans(5, 12, data, "monkey")

    dataset = pd.read_csv(f'bases/monkey.txt', sep = '\t')
    datasetRead = pd.read_csv(f'generated/monkey.clu', sep = '\t', names=["sample_label", "class"])

    pyplot.scatter(dataset['D1'].values, dataset['D2'].values, c = datasetRead['class'].values) 
    pyplot.savefig(f'grafico_monkey_C2.jpg')

    pyplot.scatter(dataset['D1'].values, dataset['D2'].values) 
    pyplot.savefig(f'grafico_geral_monkey.jpg')

    resultRead = pd.read_csv(f'generated/monkeyReal.clu', sep = '\t', names=["sample_label", "class"])

    file = open('generated/Resultado_monkey.txt', 'w')

    x = datasetRead['class'].values
    y = resultRead['class'].values

    rand = adjusted_rand_score(x,y)
    file.write("Indice Rand - " + ' ' + "monkey" + ' = ' + str(round(rand, 4)) + '\n')

main()
