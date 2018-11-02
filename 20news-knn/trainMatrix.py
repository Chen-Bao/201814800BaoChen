import constMatrix

documentPath = "D:/Coding/Data Mining/20news/processedDoc.txt"

dictionaryPath="D:/Coding/Data Mining/20news/dic.txt"

tfPath="D:/Coding/Data Mining/20news/tf.txt"

idfPath="D:/Coding/Data Mining/20news/idf.txt"

docContent=constMatrix.inputDoc(documentPath)
dictionary=constMatrix.inputDic(dictionaryPath)
tf=constMatrix.inputTF(tfPath)
idf=constMatrix.inputIDF(idfPath)

#print(len(documents))
#print(len(dictionary))

documentMatrix=constMatrix.constructMatrix(docContent,dictionary,tf,idf)

ff = open("matrix-training.txt", "w",encoding='ISO-8859-1')
for i in range(len(docContent)):
    documentVector=documentMatrix[i]
    #print(documentVector)
    for j in range(len(dictionary)):
        ff.write('%s ' % documentVector[j])
    ff.write("\n")
ff.close()