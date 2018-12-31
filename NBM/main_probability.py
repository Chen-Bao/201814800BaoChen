wordCountPath = "wordCount.txt"
wordCount=[]
ff=open(wordCountPath,'w',encoding='ISO-8859-1')

for i in range(20):
    filePath="processedDoc/processedDoc_"+str(i)+".txt"
    f1=open(filePath,encoding='ISO-8859-1')
    documents=f1.readlines()
    f1.close()

    docVec=[]
    wordCount.append(0)
    for document in documents:
        document=document.strip("\n").split()
        docVec.append(document[1:])
        wordCount[i]+=len(document)-1

    proDic={}
    for wordVec in docVec:
        for word in wordVec:
            if word not in proDic:
                proDic[word]=1
            else:
                proDic[word]+=1

    ff.write("%d\n" % wordCount[i])
    proPath="probability/probability_"+str(i)+".txt"
    f2=open(proPath,'w',encoding="ISO-8859-1")
    probability={}
    for word in proDic:
        probability[word]=proDic[word]
        f2.write("%s %f\n" % (word,probability[word]))
    f2.close()
ff.close()