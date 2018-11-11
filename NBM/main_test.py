import os
import math

def takeSecond(elem):
    return elem[1]

f1=open("test_processedDoc.txt",encoding='ISO-8859-1')
processedTest=f1.readlines() # the processed document that were split in to words

f2=open("cateProbability.txt",encoding='ISO-8859-1')
cateProbability=f2.readlines() # the probability of each category
newCate=[]
for cate in cateProbability:
    newCate.append(float(cate.strip('\n')))
cateProbability=newCate

f3=open("wordCount.txt",encoding='ISO-8859-1')
wordCount=f3.readlines() # the number of words in each document
newcount=[]
for count in wordCount:
    newcount.append(int(count.strip("\n")))
wordCount=newcount

filePath="E:/Coding/Data Mining/NBM/probability"
files=os.listdir(filePath) # the probability of each word in each document of the training data

probList=[]
for file in files:
    f4=open(filePath+"/"+file,encoding='ISO-8859-1')
    probabilities=f4.readlines()
    docProb={}
    for probability in probabilities:
        probability=probability.strip("\n").split()
        docProb[probability[0]]=float(probability[1])
    probList.append(docProb)
    f4.close()

f5=open("test_result.txt","w")
for document in processedTest:
    document=document.strip("\n").split()
    documentProb=[]
    for i in range(len(probList)):
        P_doc = 0
        for word in document[1:]:
            if word in probList[i]:
                #print(probList[i][word])
                #print((probList[i][word]+1)/(wordCount[i]+len(probList[i])))
                #print(math.log((probList[i][word]+1)/(wordCount[i]+len(probList[i]))))

                P_doc+=math.log((probList[i][word]+1)/(wordCount[i]+len(probList[i])))
            else:
                P_doc+=math.log(1/len(probList[i]))
            #print(P_doc)
        #print("HELLO")
        P_doc=P_doc+math.log(cateProbability[i])
        documentProb.append((i,P_doc))
    documentProb.sort(key=takeSecond,reverse=True)
    print(documentProb[0][0])
    f5.write("%d\n" % documentProb[0][0])
f5.close()