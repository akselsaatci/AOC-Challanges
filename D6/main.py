with open('data.txt', "r") as datafile:
    dataText = datafile.read()

for i in range(len(dataText) - 14):
    kir = False
    newData = dataText[i:i + 14]
    for a in range(len(newData)):
        toplam = 0
        for b in newData[a + 1:]:
            if newData[a] == b:
                kir = True
                break
        if kir:
            break
    if kir == False:
        print(i + 14)
        break
