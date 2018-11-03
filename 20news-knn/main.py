import process
from collections import Counter

#input data
path = "D:/Coding/Data Mining/20news-18828"

fileList = []  # the list of files
tfDocumentList=[]#the list of tf values of documents within one single file
flag=0 #flag=0, training
document_count=process.docProcess(path,fileList,tfDocumentList,flag)

tf3000List=[]
f5=open("train/3000.txt","w",encoding='ISO-8859-1')
for file in fileList:
    for i in range(150):
        tf = {}
        count=Counter(file[i])
        for j in range(len(file[i])):
            if file[i][j] not in tf:
                currentWordFre=count[file[i][j]]
                tf[file[i][j]] = currentWordFre / len(file[i])  # tf value of appeared word in one single document
            f5.write("%s " % (file[i][j]))
        tf3000List.append(tf)
        f5.write("\n")
f5.close()

fff = open("train/tf-3000.txt", "w", encoding='ISO-8859-1')
for document in tf3000List:
    fff.write('%s\n' % (document))
fff.close()

'''
#CountTheNumber=0

if flag==0:
    f4= open("train/processedDoc.txt", "w",encoding='ISO-8859-1')
else:
    f4 = open("test/processedDoc.txt", "w", encoding='ISO-8859-1')
for file in fileList:
    for document in file:
        for word in document:
            f4.write('%s ' % (word))
        f4.write("\n")
        #CountTheNumber+=1
f4.close()
#print(CountTheNumber)

#print(len(tfDocumentList))
#print(document_count) #15056
if flag==0:
    fff = open("train/tf.txt", "w",encoding='ISO-8859-1')
else:
    fff = open("test/tf.txt", "w", encoding='ISO-8859-1')
for document in tfDocumentList:
    fff.write('%s\n' % (document))
fff.close()

wordDic=process.createDic(fileList) # compute a dic of 'the number of documents with a certain word in it'
if flag==0:
    f = open("train/dic.txt", "w", encoding='ISO-8859-1')
else:
    f=open("test/dic.txt", "w", encoding='ISO-8859-1')
for word in wordDic:
    f.write('%s\t%d\n' % (word, wordDic[word]))
f.close()

print(document_count)
idf=process.calIDF(document_count,wordDic)

if flag==0:
    f = open("train/idf.txt", "w",encoding='ISO-8859-1')
else:
    f=open("test/idf.txt", "w",encoding='ISO-8859-1')
for word in idf:
    f.write('%s\t%9f\n' % (word, idf[word]))
f.close()
'''