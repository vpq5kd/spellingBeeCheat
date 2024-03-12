with open('words.txt', 'r') as file:
    lines = file.readlines()
row = []
for line in lines:
    if len(line) >= 5:
        row.append(line)
possible = list(input("Please input each character in today's spelling bee sin spaces and commas (i.e. abcdefg): "))
mustHave = input("Please input today's required character: ")
def testPossible(letter, possible):
    retnum = 0
    for i in possible:
        if (letter != i):
            retnum+=1
    if retnum == 7:
        return False
    return True
def testMustHave(letter, mustHave):
    if letter == mustHave:
        return True
    else:
        return False
newList = []
for each in row:
    temp = list(each)
    ks = 0
    for letter in temp:
        if testPossible(letter,possible) == False and letter!='\n':
            ks = 1
            break
    if ks == 0:
        newList.append(each)
outList = []
for each in newList:
    temp = list(each)
    for letter in temp:
        if testMustHave(letter,mustHave):
            outList.append(each)
            break
with open("spellingBeeWords.txt", "w") as file:
    for each in outList:
        file.write(each)
for each in outList:
    print(each)








