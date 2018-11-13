import os
import nltk
import string
import nltk.data

from collections import Counter

#stopwords
from nltk.corpus import stopwords
stop=stopwords.words('english')

#the stemming method
from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()

#the tokenization method
def splitIntoWords(article):
    documentWords=[]
    tokenizer=nltk.data.load('english.pickle')
    for paragraph in article:
        sentences = tokenizer.tokenize(paragraph) #first split into sentences

        for sentence in sentences:
            words=nltk.word_tokenize(sentence) #then split each sentence into words
            documentWords+=words
    return documentWords

# the pre-processing method
def preProcessing(document):
    processedDocument=[]
    iter_d=iter(document)
    for word in iter_d:
        #lowerWord=word
        lowerWord=word.lower()# change to lowercase
        word=""
        for char in lowerWord:# delete punctuation #delete numbers
            if (char not in string.punctuation) and (char not in string.digits):
                word+=char
        lowerWord=word

        #print(lowerWord)
        if len(lowerWord)==0: #the word is deleted because it only contains punctuation or numbers
            continue
        else:
            lowerWord = lemma.lemmatize(lowerWord)  # stemming
        if lowerWord in stop: # delete stop words
            continue
        elif len(lowerWord)<2: # delete words whose length is lower than 2
            continue
        else:
            processedDocument.append(lowerWord)
    return processedDocument

def docProcess(path,fileList,flag):
    files = os.listdir(path)  # obtain all file names under path [atl.atheism,comp.graphics,...]
    documents = []
    document_count=0
    category_index=0

    for file in files:
        documents=os.listdir(path+"/"+file)
        countTraining=int(len(documents)*0.8)# take the first 80% documents as the training set
        documentList=[] # the list of documents within one single file
        if flag==0:
            documentRange=range(countTraining) #training
        else:
            documentRange=range(countTraining,len(documents))

        for i in documentRange:
            document_count+=1
            currentDoc = open(path + "/" + file+"/"+documents[i],encoding='ISO-8859-1')

            wordList=splitIntoWords(currentDoc.readlines()) #tokenization

            text = nltk.Text(wordList)
            tags = nltk.pos_tag(text)
            wordVec = []
            for tag in tags:
                if "NN" in tag[1]:
                    wordVec.append(tag[0])
            #print(wordVec)

            #print(wordList)
            processedDocument=preProcessing(wordVec) #preprocessing

            documentLength = len(processedDocument) #number of words in one document
            count=Counter(processedDocument) #count the number of each word
            #print(count.most_common(10))

            processedDocument=[category_index]+processedDocument

            documentList.append(processedDocument)

        fileList.append(documentList)
        category_index+=1

    return document_count
