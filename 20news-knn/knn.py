import math
from collections import Counter

#training data
trainPath = "train/matrix-unit.txt"
testPath = "test/matrix-unit.txt"

def takeSecond(elem):
    return elem[1]

categoryList=[]
count=0

with open(testPath, encoding='ISO-8859-1') as testf:
    for testVec in testf:
    # a testing document
        testVec=testVec.strip("\n").split()
        new_vec = []
        for item in testVec[1:]:
            new_vec.append(float(item))
        testVec = new_vec
        '''turn to unit vector
        normTestVec=math.sqrt(sum([item*item for item in testVec]))
        testVec= [item / normTestVec for item in testVec]
        '''
        distanceSet = []

        with open(trainPath, encoding='ISO-8859-1') as trainf:
            for trainVec in trainf:
                trainVec=trainVec.strip("\n").split()
                #print(trainVec[0])
                #compute cosine value of two vectors
                new_vec = []
                for item in trainVec[1:]:
                    new_vec.append(float(item))
                '''
                normTrainVec = math.sqrt(sum([item * item for item in trainVec]))
                trainVec = [item / normTrainVec for item in trainVec]

                print(trainVec)
                '''
                cosVal=sum([testVec[i]*new_vec[i] for i in range(len(new_vec))])
                #print(cosVal)
                distanceSet.append((trainVec[0],cosVal))

        # find the top 100 largest cosine value (top 100 nearest vectors)
        distanceSet.sort(key=takeSecond,reverse=True)
        #print(distanceSet)
        category100=[]
        for i in range(100):
            category100.append(distanceSet[i][0])
        #print(category100)
        countingRes=Counter(category100)
        #print(countingRes)
        maxCategory=max(countingRes.items(),key=lambda x:x[1])[0] #find the category testVector belongs to
        count+=1
        print(count,maxCategory)
        #print("\n")
        categoryList.append(maxCategory)
testf.close()

f = open("test-guess-category.txt", "w", encoding='ISO-8859-1')
for item in categoryList:
    f.write('%s ' % item)
f.close()