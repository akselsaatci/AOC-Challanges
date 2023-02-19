from anytree import Node, RenderTree, search, AsciiStyle

with open('data.txt', "r") as datafile:
    dataText = datafile.read()
dataText = dataText.split("$")

currentNode = Node;
rootDic = Node("/", value=0)
for i in dataText:
    if i == "" or i == "\n":
        continue
    if i[0] == " ":
        i = i.strip()
    i = i.split("\n")
    for b in range(len(i)):
        i[b] = i[b].split(" ")
    print(i)
    if i[0][0] == "cd":
        if i[0][1] == "/":
            currentNode = rootDic
        elif i[0][1] == "..":
            currentNode = currentNode.parent
        else:
            tempNode = search.find(rootDic, filter_=lambda node: (node.name == i[0][1] and node.parent == currentNode))
            if tempNode is not None:
                currentNode = tempNode
            else:
                currentNode = Node(i[0][1], parent=currentNode, value=0)

    if i[0][0] == "ls":
        print(i)
        for c in range(len(i) - 1):
            if i[c + 1][0] == "dir":
                tempNode = search.find(rootDic,
                                       filter_=lambda node: node.name == i[c + 1][1] and node.parent == currentNode)
                if tempNode is not None:
                    currentNode = currentNode
                else:
                    Node(i[c + 1][1], parent=currentNode, value=0)
            else:
                currentNode.value = currentNode.value + int(i[c + 1][0])

currentNode = rootDic


def treeGez(a):
    if len(a.children) != 0:
        for k in a.children:
            treeGez(k)
    else:
        a.parent.value = a.parent.value + a.value


treeGez(rootDic)
sums = 0
for i in search.findall(rootDic, filter_=lambda node: node.value <= 100000):
    sums = sums + i.value
print(sums)
print(RenderTree(rootDic, style=AsciiStyle()))
