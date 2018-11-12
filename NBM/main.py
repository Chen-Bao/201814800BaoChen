import os
filePath="E:/Coding/Data Mining/20news-18828"
files=os.listdir(filePath)
documents=[]
p_category=[]
category_length=[]

categoryPath="cateProbability.txt"
f1=open(categoryPath,'w',encoding="ISO-8859-1")
for file in files:
    documents=os.listdir(filePath+"/"+file)
    category_length.append(int(len(documents)*0.8))
    p_category.append(float(int(len(documents)*0.8)/15056))

for cate in p_category:
    f1.write("%f\n" % cate)
print("各类别概率：")
print(p_category)