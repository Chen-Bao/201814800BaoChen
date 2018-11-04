ff = open("test-guess-category.txt",encoding='ISO-8859-1')
str=ff.readline()
str = str.strip("/n").split()

p_str=[]
for i in range(len(str)):
    p_str.append(float(str[i]))
ff.close()

f = open("test/matrix.txt",encoding='ISO-8859-1')
answer=f.readlines()
category=[]
for document in answer:
    document=document.strip("\n").split()
    category.append(float(document[0]))
f.close()

right=0
for i in range(len(category)):
    if p_str[i]==category[i]:
        right+=1
print(right/3772)
