list1 = ['G',
         'W',
         'L',
         'J',
         'B',
         'R',
         'T',
         'D']

list2 = ['C',
         'W',
         'S', ]

list3 = ['M',
         'T',
         'Z',
         'R']

list4 = ['V',
         'P',
         'S',
         'H',
         'C',
         'T',
         'D', ]

list5 = ['Z',
         'D',
         'L',
         'T',
         'P',
         'G', ]

list6 = ['D',
         'C',
         'Q',
         'J',
         'Z',
         'R',
         'B',
         'F', ]

list7 = ['R',
         'T',
         'F',
         'M',
         'J',
         'D',
         'B',
         'S', ]

list8 = ['M',
         'V',
         'T',
         'B',
         'R',
         'H',
         'L', ]

list9 = ['V',
         'S',
         'D',
         'P',
         'Q', ]

allList = [list1, list2, list3, list4, list5, list6, list7, list8, list9]
# list1 = [
# 'N',
# 'Z',]
#
# list2 = ['D','C',
# 'M',]
# list3 = ['P']
# allList = [list1,list2,list3]

with open('data.txt', "r") as datafile:
    dataText = datafile.read()
data = dataText.split("\n")
for i in data:
    i = i.split(" ")
    print(i)
    tempList = []
    for k in range(int(i[0])):
        tempList.insert(0, allList[int(i[1]) - 1][0])
        del allList[int(i[1]) - 1][0]
    for c in tempList:
        allList[int(i[2]) - 1].insert(0, c)
    tempList = []
for i in allList:
    print(i[0])
