# Rummikub solver
import re

colors = ['red','blue','black','yellow']
allTiles = list()
handTiles = list()

for k in range(2):
    for i in range(13):
        for j in range(len(colors)):
            allTiles.append(str(colors[j]) + str(i+1))

allTiles.sort()

allTiles.append('wild')
allTiles.append('wild')

print('These are all the tiles: ' + str(allTiles))

while True:
    userinput = input('What tiles do you have in your hand? ')
    if userinput == '':
        break
    handTiles.append(userinput)
    allTiles.remove(userinput)

# duplicate checker function
def hasDuplicates(checkList):
    return len(checkList) != len(set(checkList))

# consecutive tiles function (will sort first)
def checkConsecutive(checkList): 
    return sorted(checkList) == list(range(min(checkList), max(checkList)+1)) 

# checks for valid sets
def isSet(checkList):
    if hasDuplicates(checkList) is True:
        return False
    if len(checkList) < 3:
        return False
    colorsPresent = list()
    numbersPresent = list()
    for i in range(len(checkList)):
        colorsPresent.append(re.sub(r'\d+', '', checkList[i]))
        numbersPresent.append(re.sub(r'\w+', '', checkList[i]))
    if len(set(colorsPresent)) >= 3 and len(set(numbersPresent)) == 1:
        return True
    else:
        return False

def isRun(checkList):
    if hasDuplicates(checkList) is True:
        return False
    if len(checkList) < 3:
        return False
    colorsPresent = list()
    numbersPresent = list()
    for i in range(len(checkList)):
        colorsPresent.append(re.sub(r'\d+', '', checkList[i]))
        numbersPresent.append(re.sub(r'\w+', '', checkList[i]))
    if len(set(colorsPresent)) == 1 and checkConsecutive(checkList) == True:
        return True
    else:
        return False

print('You have these tiles: ' + str(handTiles))
print('These tiles are at-large: ' + str(allTiles))

input('wait')