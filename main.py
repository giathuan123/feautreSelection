from math import sqrt
import sys

def getDistance(x: list, y: list):
    sum = 0
    for idx, _ in enumerate(x):
        sum += (x[idx] - y[idx])**2
    return sqrt(sum)
        
def getData(i, feature):
    try:
        curData = []
        for j in feature:
            curData.append(i[j])
        return curData
    except:
        print(i)
        sys.exit()
    
def getAccuracy(data, feature):
    accuracy = 0
    for iIdx, i in enumerate(data):
        testObject = getData(i, feature)
        actualLabel = i[0]
        minDistance = float('inf')
        neigbourLabel = -1
        for jIdx, j in enumerate(data):
            if jIdx == iIdx:
                continue
            candidateObject = getData(j, feature)
            distance = getDistance(candidateObject,testObject)
            if distance < minDistance:
                minDistance = distance
                neigbourLabel = j[0]
        #     print(f"is {iIdx} nearest neighbour to {jIdx}")
        # print(f"Object {iIdx} is of class {neigbourLabel}") 
        if actualLabel == neigbourLabel:
            accuracy+=1
    return accuracy/len(data)

def search(data, numOfFeatures):
    curFeatures = []
    bestOverall = 0
    bestFeatures = []
    for i in range(1, numOfFeatures):
        print(f"On the {i} level")
        bestSoFar = 0
        for j in range(1, numOfFeatures):
            if j not in curFeatures:
                print(f"Considering adding the {j} feature")
                accuracy = getAccuracy(data, curFeatures + [j])
                if(accuracy > bestSoFar):
                    bestSoFar = accuracy
                    featureToAdd = j
        curFeatures.append(featureToAdd)
        if(bestSoFar > bestOverall):
            bestOverall = bestSoFar
            bestFeatures = [] + curFeatures
        print(bestSoFar) 
        print("On this level ", i, 'added feature', featureToAdd);
    print(bestFeatures, bestOverall) 
    print(curFeatures)

def main():
    if(len(sys.argv) != 2):
        sys.exit("USAGE: python main.py <data.txt>")
    with open(sys.argv[1]) as dataFile:
        data = []
        numOfFeatures = 0
        for lines in dataFile:
            row = [float(x) for x in filter(lambda x : x != '', lines.split(' '))]
            data.append(row)
            numOfFeatures = len(row) - 1
        search(data, numOfFeatures) 
main()            
