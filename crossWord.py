from pandas import DataFrame
import sys

fileName = "words.txt"

with open(fileName) as f:
    words = f.read().splitlines()


VERTICAL = "vertical"
HORIZONTAL = "horizontal"


def wordUpper(word):
    return word.upper()


capsWord = map(wordUpper, words)
words = list(capsWord)
matrix = [[]]


def findPosition(word):

    horizontalLength = len(matrix[0])
    verticalLength = len(matrix)

    for row in range(horizontalLength):
        isAvailable = checkRow(row, word)
        if(isAvailable != False):
            posStartWord = isAvailable
            putToMatrix(word, posStartWord, HORIZONTAL)
            return [True, posStartWord]

    for column in range(verticalLength):
        isAvailable = checkColumn(column, word)
        if(isAvailable != False):
            posStartWord = isAvailable
            putToMatrix(word, posStartWord, VERTICAL)
            return [True, posStartWord]
    return [False, None]


def checkRow(row, word):
    global matrix
    if isOutIndex(y=row) == True:
        return False
    for colMatrix in range(len(matrix[row])):
        isFit = isFitForWord(
            word, lambda iteration: [row, colMatrix + iteration])
        if isFit:
            return [row, colMatrix]

    return False


def checkColumn(column, word):
    global matrix
    if isOutIndex(x=column) == True:
        return False
    for rowMatrix in range(len(matrix)):
        isFit = isFitForWord(
            word, lambda iteration: [rowMatrix + iteration, column])
        if isFit:
            return [rowMatrix, column]

    return False


def isFitForWord(word, getChar):
    global matrix
    countNotPossible = 0
    countThroughChar = 0
    iterationWord = 0

    # Check if nothing before startPoint
    charBeforeRow, charBeforeCol = getChar(iterationWord - 1)
    if(isOutIndex(charBeforeRow, charBeforeCol) == False):
        charBefore = matrix[charBeforeRow][charBeforeCol]
        if(charBefore != ''):
            return False

    # And check if nothing after word
    charAfter = {'row': 0, 'col': 0}
    charAfter['row'], charAfter['col'] = getChar(len(word))
    if(isOutIndex(charAfter['row'], charAfter['col']) == False):
        charAfterText = matrix[charAfter['row']][charAfter['col']]
        if(charAfterText != ''):
            return False

    # Check if the word fit to the matrix from start point
    for char in word:
        charPosRow, charPosCol = getChar(iterationWord)
        iterationWord += 1
        if(isOutIndex(charPosRow, charPosCol)):
            continue

        charMatrix = matrix[charPosRow][charPosCol]
        if(charMatrix != char and charMatrix != ''):
            countNotPossible += 1
        if(charMatrix == char):

            countThroughChar += 1

    if(countNotPossible == 0 and countThroughChar > 0):
        return True
    return False


def getCell(row, col):
    global matrix
    if(isOutIndex(row, col) == False):
        return matrix[row][col]
    else:
        return ''


def isOutIndex(x=0, y=0):
    global matrix
    if(x > len(matrix) - 1):
        return True
    if(y > len(matrix[x]) - 1):
        return True
    return False


def putToMatrix(word, wordStart, direction):
    global matrix
    posX = wordStart[0]
    posY = wordStart[1]

    for char in word:
        matrix[posX][posY] = char

        if(direction == HORIZONTAL):
            posY += 1
        elif(direction == VERTICAL):
            posX += 1
    return True


def printOutMatrix():
    for x in matrix:
        row = ""
        for y in x:
            row += " "+y
        print(row)


def generateEmptyMatrix(width, height):
    global matrix
    for i in range(height):
        matrix.append([])
        for j in range(width):
            matrix[i].append('')


if __name__ == "__main__":
    wordInserted = []
    if len(sys.argv) <= 1:
        print("Masukkan lebar dan panjang kotak TTS")
        print("     contoh : python crossWord.py 10 10")
        print("     untuk lebar 10 dan panjang 10")
        exit()
    inputWidth = sys.argv[1]
    inputHeight = sys.argv[2]

    generateEmptyMatrix(int(inputWidth), int(inputHeight))

    wordImported = {}
    wordNotImported = []
    isFirst = True
    for word in words:
        if isFirst:
            # Put first word to matrix
            putToMatrix(word, [0, 0], HORIZONTAL)
            isFirst = False
            continue
        ok, positionWord = findPosition(word)
        if ok:
            wordImported[word] = positionWord
        else:
            wordNotImported.append(word)

    print(DataFrame(matrix))
    print("Sebanyak {} kata dimasukkan, yaitu :".format(len(wordImported)))
    print(wordImported)
    if len(wordNotImported) > 0:
        print("Sebanyak {} kata yang tidak dimasukkan yaitu :".format(
            len(wordNotImported)))
        print(wordNotImported)
