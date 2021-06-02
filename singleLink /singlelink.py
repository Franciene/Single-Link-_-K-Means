import math as math
from scipy.spatial import distance
import pandas as pd

class dataset:
    def __init__(self, nome, data, cluster):
        self.nome = nome
        self.data = data
        self.cluster = cluster

class distanceData:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

def sorting(elem):
    return elem.dist

def minDist(i, j):
    if(i == j):
        return 0
    distancia = math.inf
    for a in i:
        for b in j:
            x = distance.euclidean(a.data, b.data)
            if (distancia > x):
                distancia = x
    return round(distancia, 4)

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
            datasetObject = dataset(nome, element, c)
            dataSet.append(datasetObject)
            c += 1
        element = []
    file.close()
    return dataSet

def singleLinkClustering(min, max, path, nameDataSet):
    data = readDataSet(path)
    # data = pd.read_csv(f'{path}', sep = '\t', names=["sample_label", "class"])
    # print(data)
    clusterSize = len(data)
    clusters = [[i] for i in data]

    while(clusterSize > min):
        list = []
        x = 0
        for i in clusters:
            y = 0
            for j in clusters:
                if(x > y):
                    dist = minDist(i, j)
                    aux = distanceData(x, y, dist)
                    list.append(aux)
                y = y+1
            x = x+1
        list.sort(key=sorting)
        clusters[list[0].x] += clusters[list[0].y]
        del(clusters[list[0].y])
        clusterSize = clusterSize - 1
        if(clusterSize <= max):
            file = open('clusterFiles/singleLink/' + nameDataSet + str(clusterSize) + '.clu', 'w')
            n = 0
            for i in clusters:
                for l in i:
                    for k in data:
                        if l.nome == k.nome:
                            k.cluster = n
                            break
                n += 1

            for each in data:
                file.write(str(each.nome) + '\t' + str(each.cluster)+'\n')
