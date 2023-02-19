import string
with open('data.txt', "r") as datafile:
    dataText = datafile.read()
data = dataText.split("\n")

sumPoints = 0
charPoints = {**{chr(i + 96): i for i in range(1, 27)}, **{chr(i+64):i+26 for i in range(1,27)}}
for c in data:
    str1 = c
    strLen = int(len(str1) / 2)
    firsC = str1[:strLen]
    secondC = str1[strLen:]

    for i in firsC:
        bittimi = 0
        for a in secondC:
            if i == a:
                sumPoints = sumPoints + charPoints.get(i)
                bittimi = 1
                break
        if bittimi == 1:
            break
print(sumPoints)