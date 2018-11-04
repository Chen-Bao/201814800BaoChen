import math

#Path = "train/matrix.txt"
Path = "test/matrix.txt"

matrix=[]
count=0
trainCount=200
with open(Path, encoding='ISO-8859-1') as f:
    for vec in f:
    # a testing document
        vec=vec.strip("\n").split()
        new_vec = []
        label=int(vec[0])
        for item in vec[1:]:
            new_vec.append(float(item))
        vec = new_vec
        #print(vec)
        #turn to unit vector
        normVec=math.sqrt(sum([item*item for item in vec]))
        vec= [item / normVec*10000 for item in vec]
        vec=[label]+vec
        count+=1
        print(count)
        matrix.append(vec)
f.close()

ff = open("test/matrix-unit.txt", "w", encoding='ISO-8859-1')
for vec in matrix:
    for item in vec:
        ff.write('%f ' % item)
    ff.write("\n")
ff.close()