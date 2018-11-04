import constMatrix

flag=0 # flag=0 training

if flag==0:
    documentPath = "train/3000.txt"
else:
    documentPath = "test/processedDoc.txt"

if flag == 0:
    dictionaryPath="train/dic.txt"
else:
    dictionaryPath = "train/dic.txt"

if flag==0:
    tfPath="train/tf-3000.txt"
else:
    tfPath = "test/tf.txt"

if flag==0:
    idfPath="train/idf.txt"
else:
    idfPath = "test/idf.txt"

docContent=constMatrix.inputDoc(documentPath)
dictionary=constMatrix.inputDic(dictionaryPath)
tf=constMatrix.inputTF(tfPath)
idf=constMatrix.inputIDF(idfPath)

documentMatrix=constMatrix.constructMatrix(docContent,dictionary,tf,idf)
if flag==0:
    ff = open("train/matrix.txt", "w",encoding='ISO-8859-1')
else:
    ff = open("test/matrix.txt", "w", encoding='ISO-8859-1')

for i in range(len(docContent)):
    documentVector=documentMatrix[i]
    #print(documentVector)
    for j in range(len(dictionary)):
        ff.write('%s ' % documentVector[j])
    ff.write("\n")
ff.close()