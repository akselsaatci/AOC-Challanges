with open('data.txt', "r") as datafile:
    dataText = datafile.read()
data = dataText.split("\n")
print(data)
sumPoints = 0
charPoints = {**{chr(i + 96): i for i in range(1, 27)}, **{chr(i + 64): i + 26 for i in range(1, 27)}}
for c in range(0, int(len(data)), 3):
    for i1 in data[c]:
        bittimi = 0
        for i2 in data[c + 1]:
            for i3 in data[c + 2]:
                if i1 == i2 == i3:
                    sumPoints = sumPoints + charPoints[i1]
                    bittimi = 1
                    break
            if bittimi == 1:
                break
        if bittimi == 1:
            break

print(sumPoints)
