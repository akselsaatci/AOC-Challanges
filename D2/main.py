# A X Rock 1 Point
# B Y Paper 2 Point
# C Z Scissors 3 Point
# Lose 0 Draw 3 Win 6

# X Lose
# Y Draw
# Z Win

with open('data.txt', "r") as datafile:
    dataText = datafile.read()
data = dataText.split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" ")

points = 0

for i in data:
    if i[1] == "X":
        points = points + 1
        if i[0] == "A":
            points = points + 3
        elif i[0] == "B":
            points = points + 0
        elif i[0] == "C":
            points = points + 6

    if i[1] == "Y":
        points = points + 2
        if i[0] == "A":
            points = points + 6
        elif i[0] == "B":
            points = points + 3
        elif i[0] == "C":
            points = points + 0

    if i[1] == "Z":
        points = points + 3
        if i[0] == "A":
            points = points + 0
        elif i[0] == "B":
            points = points + 6
        elif i[0] == "C":
            points = points + 3

print(points)