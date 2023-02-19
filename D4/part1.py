with open('data.txt', "r") as datafile:
    dataText = datafile.read()
data = dataText.split("\n")
print(data)
count = 0
for i in data:
    i = i.split(",")
    for a in i:
        a = a.split("-")
for i in data:
    i = i.split(",")
    for a in i:
        i[i.index(a)] = a.split("-")
    if int(i[0][0]) <= int(i[1][0]) and int(i[0][1]) >= int(i[1][1]):
        print(i)
        count = count + 1
        continue
    if int(i[1][0]) <= int(i[0][0]) and int(i[1][1]) >= int(i[0][1]):
        print(i)
        count = count + 1
        continue
print(count)
