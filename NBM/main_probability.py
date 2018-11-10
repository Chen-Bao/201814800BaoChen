filePath='processedDoc/processedDoc_19.txt'
f1=open(filePath,encoding='ISO-8859-1')
documents=f1.readlines()
f1.close()

docVec=[]
wordCount=0
for document in documents:
    document=document.strip("\n").split()
    docVec.append(document[1:])
    wordCount+=len(document)-1

proDic={}
for wordVec in docVec:
    for word in wordVec:
        if word not in proDic:
            proDic[word]=1
        else:
            proDic[word]+=1

proPath="probability/probability_19.txt"
f2=open(proPath,'w',encoding="ISO-8859-1")
probability={}
for word in proDic:
    probability[word]=proDic[word]/wordCount
    f2.write("%s %f\n" % (word,probability[word]))