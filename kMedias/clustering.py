import math as math
import random as random
import numpy as numpy
from scipy.spatial import distance


class objects:
    def __init__(self, nome, data, cluster):
        self.nome = nome
        self.data = data
        self.closest = self
        self.cluster = cluster


class ot:
    def __init__(self, a, b, y):
        self.a = a
        self.b = b
        self.y = y

def sorting(elem):
    return elem.y

def readDataSet(nameDataSet):
    path = nameDataSet
    file = open(path)
    element = []
    dataSet = []
    nome = ''
    c = 0
    for line in file:
        for word in line.split():
            if(word == 'sample_label'):
                break
            else:
                if(line.split().index(word) == 0):
                    nome = word
                else:
                    element.append(float(word))
        if(element):
            novoObjeto = objects(nome, element, c)
            dataSet.append(novoObjeto)
            c += 1
        element = []
    file.close()
    return dataSet    

def printPartition(path, cluster):
    file = open(path, 'w')
    for each in cluster:
        file.write(str(each.nome) + '\t' + str(each.cluster)+'\n')

def kMeans(nClusters, nIterations, path, nameDataSet):
    data = readDataSet(path)  # array com objects
    rows = len(data)  # int com a quantidade de linhas

    # inicializa os centroides
    centroids = []
    for i in range(nClusters):
        centroids.append(data[random.randint(0, rows-1)])

    # inicializa dataCentroid com [] para ser uzada em findCentroidForDataPoint
    dataCentroid = []
    for i in range(rows):
        # array de int com o numero do centroid para cada posicao de dado
        dataCentroid.append([])

    # inicializa cada dado para seu respectivo centroide
    iteradorAuxiliar = rows
    for dataPos in range(iteradorAuxiliar):
        for i in range(nClusters):
            if(dataCentroid[dataPos] == []):
                dataCentroid[dataPos] = i

            distanceNow = float(distance.euclidean(
                centroids[dataCentroid[dataPos]].data, data[dataPos].data))

            newDistance = float(distance.euclidean(
                centroids[i].data, data[dataPos].data))

            if(distanceNow > newDistance):
                dataCentroid[dataPos] = i

    partitions = [[]for i in range(nClusters)]
    for j in range(iteradorAuxiliar):
        partitions[dataCentroid[j]].append(data[j])

    count = 0
    for i in range(nIterations):
        count += 1
        a = 0
        for p in partitions:
            x = 0
            y = 0
            l = 0
            for d in p:
                x += d.data[0]
                y += d.data[1]
                l += 1
            if l == 0:
                l = 1
            centroids[a].data[0] = x/l
            centroids[a].data[1] = y/l
            a = a+1
        for dataPos in range(rows):
            for index in range(nClusters):
                if(dataCentroid[dataPos] == []):
                    dataCentroid[dataPos] = index

                distanceNow = float(distance.euclidean(
                    centroids[dataCentroid[dataPos]].data, data[dataPos].data))

                newDistance = float(distance.euclidean(
                    centroids[index].data, data[dataPos].data))

                if(distanceNow > newDistance):
                    dataCentroid[dataPos] = index

        partitions = [[]for i in range(nClusters)]  # reset partitions
        for j in range(rows):
            partitions[dataCentroid[j]].append(
            data[j])  # findin new partitions

    for j in range(rows):
        data[j].cluster = dataCentroid[j]

    pat = "generated/" + nameDataSet + '.clu'

    if(nameDataSet == 'monkey'):
        for d in data:
            d.cluster += 1
    printPartition(pat, data)        







