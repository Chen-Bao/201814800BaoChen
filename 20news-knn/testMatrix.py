import constMatrix

documentPath = "test/processedDoc.txt"

dictionaryPath="train/dic.txt"

tfPath="test/tf.txt"

idfPath="test/idf.txt"

docContent=constMatrix.inputDoc(documentPath)
dictionary=constMatrix.inputDic(dictionaryPath)
tf=constMatrix.inputTF(tfPath)
idf=constMatrix.inputIDF(idfPath)

print(len(docContent))
print(len(dictionary))

documentMatrix=constMatrix.constructMatrix(docContent,dictionary,tf,idf)

ff = open("test/matrix.txt", "w",encoding='ISO-8859-1')
for i in range(len(docContent)):
    documentVector=documentMatrix[i]
    for j in range(len(dictionary)):
        ff.write('%s ' % documentVector[j])
    ff.write("\n")
ff.close()