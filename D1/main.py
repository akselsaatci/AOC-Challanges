with open('data.txt', "r") as datafile:
    dataText = datafile.read()
dataText = dataText.strip().split("\n\n")
new = []
for i in dataText:
    i = i.split("\n")
    new.append(list(map(int,i)))

sumList = []
for i in new:
    tempSum = 0
    for item in i:
        tempSum = tempSum + item
    sumList.append(tempSum)
topThree = []
for i in range(3):
    key = sumList.index(max(sumList))
    topThree.append(sumList[key])
    del sumList[key]
print(sum(topThree))
