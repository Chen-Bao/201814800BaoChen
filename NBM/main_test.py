import os
import math

def takeSecond(elem):
    return elem[1]

f1=open("test_processedDoc.txt",encoding='ISO-8859-1')
processedTest=f1.readlines() # the processed testing document that were split in to words

f2=open("cateProbability.txt",encoding='ISO-8859-1')
cateProbability=f2.readlines() # the prior probability of each category
newCate=[]
for cate in cateProbability:
    newCate.append(float(cate.strip('\n')))
cateProbability=newCate

f3=open("wordCount.txt",encoding='ISO-8859-1')
wordCount=f3.readlines() # the number of words in each category
newcount=[]
for count in wordCount:
    newcount.append(int(count.strip("\n")))
wordCount=newcount

#################################
filePath="D:/Coding/Data Mining/NBM/probability"
dictionary={}
probList=[] # the number of each word in each category of the training data. (word,categoryFrequency)
for i in range(20):
    f4=open(filePath+"/probability_"+str(i)+".txt",encoding='ISO-8859-1')
    probabilities=f4.readlines()
    docProb={}
    for probability in probabilities:
        probability=probability.strip("\n").split()
        if probability[0] not in dictionary:
            dictionary[probability[0]]=1
            #print(probability[0])
        docProb[probability[0]]=float(probability[1])
    probList.append(docProb)
    f4.close()
#print(len(dictionary))
#################################
classifiedCate=[]
initialCate=[]
f5=open("test_result.txt","w")
for document in processedTest:
    document=document.strip("\n").split()
    #print(document)
    documentProb=[]
    initialCate.append(int(document[0]))
    for i in range(len(probList)):
        P_doc = 0
        for word in document[1:]:
            if word in probList[i]:
                P_doc+=math.log((probList[i][word]+1)/(wordCount[i]+len(dictionary)))
            else:
                P_doc+=math.log(1/(wordCount[i]+len(dictionary)))
            #print(P_doc)
        #print("HELLO")
        P_doc=P_doc+math.log(cateProbability[i])
        documentProb.append((i,P_doc))
    documentProb.sort(key=takeSecond,reverse=True)
    classifiedCate.append(documentProb[0][0])
    #print(documentProb[0][0])
    f5.write("%d\n" % documentProb[0][0])
f5.close()

accurate=0
for i in range(len(initialCate)):
    if initialCate[i]==classifiedCate[i]:
        accurate+=1
print(accurate/len(initialCate))