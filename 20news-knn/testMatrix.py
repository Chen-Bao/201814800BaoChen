import constMatrix

documentPath = "D:/Coding/Data Mining/20news/processedDoc.txt"

dictionaryPath="D:/Coding/Data Mining/20news/train-dic.txt"

tfPath="D:/Coding/Data Mining/20news/tf.txt"

idfPath="D:/Coding/Data Mining/20news/idf.txt"

docContent=constMatrix.inputDoc(documentPath)
dictionary=constMatrix.inputDic(dictionaryPath)
tf=constMatrix.inputTF(tfPath)
idf=constMatrix.inputIDF(idfPath)

print(len(docContent))
print(len(dictionary))

documentMatrix=constMatrix.constructMatrix(docContent,dictionary,tf,idf)

ff = open("matrix-test.txt", "w",encoding='ISO-8859-1')
for i in range(len(docContent)):
    documentVector=documentMatrix[i]
    for j in range(len(dictionary)):
        ff.write('%s ' % documentVector[j])
    ff.write("\n")
ff.close()