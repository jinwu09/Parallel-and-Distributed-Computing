import random

rangeData = [ 6000,4000,2000,500]

for maxRange in rangeData:
    dataArray = []
    for i in range(maxRange):
        dataArray.append(random.randint(0,maxRange))
    with open(f"./miniResearch/data/data{maxRange}.txt",'w') as f :
        f.write(str(dataArray))