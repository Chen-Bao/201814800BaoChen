import math
from collections import Counter

#training data
trainPath = "D:/Coding/Data Mining/20news/matrix-training.txt"
testPath = "D:/Coding/Data Mining/20news/matrix-test.txt"

testf=open(testPath,encoding='ISO-8859-1')

def takeSecond(elem):
    return elem[1]

categoryList=[]

while True:
    testVec=testf.readline() # a testing document
    if not testVec:
        break
    else:
        testVec.strip("\n")
        testVec = testVec.split()
        distanceSet = []
        trainf = open(trainPath, encoding='ISO-8859-1')
        while True:
            trainVec = trainf.readline()
            if not trainVec:
                break
            else:
                trainVec.strip("\n")
                trainVec = trainVec.split()

                #compute cosine value of two vectors
                cosVal=0
                dotMul = 0
                normTrain=0
                normTest=0
                for i in range(1,len(trainVec)):
                    dotMul += float(trainVec[i])*float(testVec[i])
                    normTrain+=math.pow(float(trainVec[i]),2)
                    normTest+=math.pow(float(testVec[i]),2)
                normTrain=math.sqrt(normTrain)
                normTest=math.sqrt(normTest)
                cosVal=abs(dotMul)/(normTrain*normTest)
                #print(cosVal)
                distanceSet.append((trainVec[0],cosVal))
        trainf.close()

        # find the top 100 largest cosine value (top 100 nearest vectors)
        distanceSet.sort(key=takeSecond,reverse=True)
        #print(distanceSet)
        category100=[]
        for i in range(100):
            category100.append(distanceSet[i][0])
        #print(category100)
        countingRes=Counter(category100)
        maxCategory=max(countingRes.items(),key=lambda x:x[1])[0] #find the category testVector belongs to
        print(maxCategory)
        #print("\n")
        categoryList.append(maxCategory)
testf.close()

f = open("test-guess-category.txt", "w", encoding='ISO-8859-1')
for item in categoryList:
    f.write('%s ' % item)
f.close()