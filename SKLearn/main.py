from sklearn.cluster import KMeans
f1=open("tf.txt")
tfContent=f1.readlines()
tf=[]
for i in range(len(tfContent)):
    tf.append(eval(tfContent[i]))
    for value in tf[i]:
        tf[i][value] = float(tf[i][value])
        #print(tf[i][value])
print(tf)

f2=open("idf.txt")
idf=f2.readlines()
idfDic={}
for word in idf:
    word=word.strip("\n")
    #print(word)
    a=word.split(" ")
    idfDic[a[0]]=float(a[1])
print(idfDic)

ff=open("category.txt")
cate_content=ff.readlines()
category=[]
for cate in cate_content:
    category.append(int(cate.strip("\n")))
print(category)
cateDic = {}
for cate in  category:
    if cate in cateDic:
        continue;
    else:
        cateDic[cate]=0
cateDicLength=len(cateDic)
print(cateDicLength)

f3=open("processedDoc.txt")
content=f3.readlines()
con=[]
for i in range(len(content)):
    item=content[i].strip("\n")
    splitItem=item.split(" ")
    con.append(splitItem[0:len(splitItem)-1])
print(con)

documentMatrix=[]
key=list(idfDic.keys())
for i in range(len(con)):
    documentVector=[]
    for j in range(len(idfDic)):
        documentVector.append(0)
    for k in range(len(idfDic)):
        word=key[k]
        if word in con[i] and word in key:
            documentVector[k]=tf[i][word]*idfDic[word]
    #print(documentVector)
    documentMatrix.append(documentVector)

num_clusters=cateDicLength#89
km_cluster=KMeans(n_clusters=num_clusters,init='k-means++')

result=km_cluster.fit_predict(documentMatrix)
print(result)
f1=open("kmeans_cluster.txt","w")
for res in result:
    f1.write("%s\n"%res)
f1.close()
