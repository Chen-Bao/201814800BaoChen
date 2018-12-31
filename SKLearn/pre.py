import math

f1=open("Tweets.txt")
tweets=f1.readlines()
numOfDocuments=len(tweets) # number of total documents in this dataset
#print(numOfDocuments)
cate_tweets=[]#documents with the sign of cluster
for i in range(150):
    cate_tweets.append(0)


for tweet in tweets:
    splitTweet=tweet.split(":")
    body=splitTweet[1].split(",")
    content=body[0].strip('\"')
    content=content.strip(' \"')
    cluster=splitTweet[2].strip("\n")
    cluster=int(cluster.strip("}"))
    #print(cluster)
    if(cate_tweets[cluster]==0):
        cate_tweets[cluster]=[]
        cate_tweets[cluster].append(content)
    else:
        cate_tweets[cluster].append(content)
#print(cate_tweets)

pure_tweets={}
numInDoc={} # number of words in one Document
pure_doc=[] #Pure documents without the sign of cluster
for i in range(len(cate_tweets)):
    if cate_tweets[i]==0:
        continue
    else:
        oneCluster=[]
        numInDoc[i]=[]
        for j in range(len(cate_tweets[i])):
            split_cate=cate_tweets[i][j].split(" ")
            oneCluster.append(split_cate)
            numInDoc[i].append(len(split_cate))
            pure_doc.append(split_cate)
        pure_tweets[i]=oneCluster
print(pure_tweets)
print(pure_doc)
print(numInDoc)

f2=open("tf.txt","w")
f3=open("idf.txt","w")
ff=open("category.txt","w")
f4=open("processedDoc.txt","w")
freq_tweets={}
def preProcess(pure_tweets,numInDoc,pure_doc):
    wordDic={} # the Dictionary of all words appeared

    for cluster in pure_tweets:
        for documents in pure_tweets[cluster]:
            for word in documents:
                if word not in wordDic:
                    wordDic[word]=1
                else:
                    wordDic[word]+=1
    idfDic = {}
    for word in list(wordDic.keys()):
        if wordDic[word]<10:#delete those words that appear less than 3 times in the whole dataset
            del wordDic[word]
        else:
            idfDic[word] = 0

    #calculate tf value
    tf_tweets= {}
    for cluster in pure_tweets:
        freq_documents = {}
        tf=[]
        for i in range(len(pure_tweets[cluster])):
            document_tf = {}
            for word in pure_tweets[cluster][i]:
                if word not in freq_documents:
                    freq_documents[word]=1
                else:
                    freq_documents[word]+=1
            for word in pure_tweets[cluster][i]:
                document_tf[word]=(freq_documents[word]/numInDoc[cluster][i])
            tf.append(document_tf)
        #print(tf)
        tf_tweets[cluster]=tf

    #print(tf_tweets)
    for cluster in tf_tweets:
        for documents in tf_tweets[cluster]:
            ff.write("%s\n" % cluster)
            f2.write("%s\n"%documents)
    f2.close()
    ff.close()
    for doc in pure_doc:
        for word in doc:
            if word in idfDic:
                f4.write("%s "% word)
        f4.write("\n")
    f4.close()
    #calculate idf value
    for word in idfDic:
        for doc in pure_doc:
            if word in doc:
                idfDic[word]+=1
            else:
                continue

        #print(numOfDocuments/idfDic[word])
        idfDic[word]=math.log(numOfDocuments/idfDic[word],10)
        #print(idfDic[word])
        f3.write("%s %f\n" % (word,idfDic[word]))
    f3.close()
    return wordDic

wordDic=preProcess(pure_tweets,numInDoc,pure_doc)
#print(wordDic)
