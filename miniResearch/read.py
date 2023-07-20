data = ""
with open(f"./miniResearch/data/data10.txt", 'r') as f:
    data = f.read()
data = data.replace('[', '')
data = data.replace(']', '')
data = data.split(', ')
IntData = []
for i in data:
    IntData.append(int(i))

print(f"meow {IntData}")