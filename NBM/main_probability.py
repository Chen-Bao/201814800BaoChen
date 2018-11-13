#calculate the conditional probability of each word in each category
wordCountPath = "wordCount.txt"
wordCount=[] # the number of words of all documents in a single category
ff=open(wordCountPath,'w',encoding='ISO-8859-1')

totalLength=0

for i in range(20):
    filePath="processedDoc/processedDoc_"+str(i)+".txt"
    f1=open(filePath,encoding='ISO-8859-1')
    documents=f1.readlines()
    f1.close()

    docVec=[] # the list of the split documents
    wordCount.append(0)
    for document in documents:
        document=document.strip("\n").split()
        docVec.append(document[1:])
        wordCount[i]+=len(document)-1
    totalLength+=wordCount[i]

    proDic={} # the dictionary of a category
    for wordVec in docVec:
        for word in wordVec:
            if word not in proDic:
                proDic[word]=1
            else:
                proDic[word]+=1

    ff.write("%d\n" % wordCount[i])

    # output the number of each word in one single category
    proPath="probability/probability_"+str(i)+".txt"
    f2=open(proPath,'w',encoding="ISO-8859-1")
    probability={}
    for word in proDic:
        if proDic[word]>=5:
            probability[word]=proDic[word]
            f2.write("%s %f\n" % (word,probability[word]))
    f2.close()
ff.close()

# compute prior probability of each category
priorProb=[]
for i in range(20):
    categoryPath = "cateProbability.txt"
    f1 = open(categoryPath, 'w', encoding="ISO-8859-1")
    priorProb.append(wordCount[i]/totalLength)
    for cate in priorProb:
        f1.write("%f\n" % cate)
#print(priorProb)