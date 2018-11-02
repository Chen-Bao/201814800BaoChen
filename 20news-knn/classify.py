import os
import math
import process

#input data
path = "D:/Coding/Data Mining/testnews"

fileList = []  # the list of files
tfDocumentList=[]#the list of tf values of documents within one single file
flag=1 #flag=1, testing
document_count=process.docProcess(path,fileList,tfDocumentList,flag)

#CountTheNumber=0
f4= open("processedDoc.txt", "w",encoding='ISO-8859-1')
for file in fileList:
    for document in file:
        for word in document:
            f4.write('%s ' % (word))
        f4.write("\n")
        #CountTheNumber+=1
f4.close()
#print(CountTheNumber)

#print(len(tfDocumentList))
print(document_count)

fff = open("tf.txt", "w",encoding='ISO-8859-1')
for document in tfDocumentList:
    fff.write('%s\n' % (document))
fff.close()

wordDic=process.createDic(fileList) # compute a dic of 'the number of documents with a certain word in it'

print(document_count)
idf=process.calIDF(document_count,wordDic)

f = open("idf.txt", "w",encoding='ISO-8859-1')
for word in idf:
    f.write('%s\t%9f\n' % (word, idf[word]))
f.close()