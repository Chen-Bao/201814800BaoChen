import constMatrix

documentPath = "train/3000.txt"

dictionaryPath="train/dic.txt"

tfPath="train/tf-3000.txt"

idfPath="train/idf.txt"

docContent=constMatrix.inputDoc(documentPath)
dictionary=constMatrix.inputDic(dictionaryPath)
tf=constMatrix.inputTF(tfPath)
idf=constMatrix.inputIDF(idfPath)

#print(len(documents))
#print(len(dictionary))

documentMatrix=constMatrix.constructMatrix(docContent,dictionary,tf,idf)

ff = open("train/matrix.txt", "w",encoding='ISO-8859-1')
for i in range(len(docContent)):
    documentVector=documentMatrix[i]
    #print(documentVector)
    for j in range(len(dictionary)):
        ff.write('%s ' % documentVector[j])
    ff.write("\n")
ff.close()