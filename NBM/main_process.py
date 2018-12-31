#pre-processing the data
import process

#input data
path = "D:/Coding/Data Mining/20news-18828"

fileList = []  # the list of files

flag=1 #flag=0, training

document_count=process.docProcess(path,fileList,flag)

#output
if flag==0:
    f4= open("train_processedDoc.txt", "w",encoding='ISO-8859-1')
else:
    f4 = open("test_processedDoc.txt", "w", encoding='ISO-8859-1')
for file in fileList:
    for document in file:
        for word in document:
            f4.write('%s ' % (word))
        f4.write("\n")
f4.close()
