#construct topic model

#input document data
def inputDoc(documentPath):
    documents = open(documentPath, encoding='ISO-8859-1').readlines()
    docContent = []
    for document in documents:
        words = document.split(" ")
        #print(words)
        words = words[0:(len(words) - 1)]
        #print(words)
        docContent.append(words)
    return docContent

#input dictionary data
def inputDic(dictionaryPath):
    dictionary = open(dictionaryPath, encoding='ISO-8859-1').readlines()
    return dictionary

#input tf values
def inputTF(tfPath):
    tf = open(tfPath, encoding='ISO-8859-1').readlines()
    for i in range(len(tf)):
        tf[i] = eval(tf[i])
        for value in tf[i]:
            tf[i][value] = float(tf[i][value])
            # print(tf[i][value])
    return tf

#input idf values
def inputIDF(idfPath):
    idfVal = open(idfPath, encoding='ISO-8859-1').readlines()
    idf = {}
    for i in range(len(idfVal)):
        singleVal = idfVal[i].split("\t")
        idf[singleVal[0]] = float(singleVal[1][0:(len(singleVal[1]) - 1)])
        # print(idf[singleVal[0]])
    return idf

def constructMatrix(docContent,dictionary,tf,idf):
    documentMatrix = []
    for i in range(len(docContent)):
        # vector initialization
        documentVector=[]
        for j in range(len(dictionary)):
            documentVector.append(0)

        # calculate vector value
        for k in range(len(dictionary)):
            wordAndFre=dictionary[k].split("\t")
            word=wordAndFre[0]
            #print(word)
            #print(tf[i])
            if word in docContent[i] and word in list(idf.keys()):
                documentVector[k]=tf[i][word]*idf[word]
        #print(documentVector)
        documentVector=[docContent[i][0]]+documentVector
        #print(documentVector)
        documentMatrix.append(documentVector)
    return documentMatrix
