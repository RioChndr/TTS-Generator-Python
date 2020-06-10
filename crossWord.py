from pandas import *
words = [
    'rio',
    'iotio',

]
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
        print("test row {}".format(row))
        isAvailable = checkRow(row, word)
        if(isAvailable != False):
            posStartWord = isAvailable
            print('kata {} di horizontal dengan posisi {}'.format(
                word, posStartWord))
            return putToMatrix(word, posStartWord, HORIZONTAL)

    for column in range(verticalLength):
        print("test column {}".format(column))
        isAvailable = checkColumn(column, word)
        if(isAvailable != False):
            posStartWord = isAvailable
            print('kata {} di horizontal dengan posisi {}'.format(
                word, posStartWord))
            return putToMatrix(word, posStartWord, VERTICAL)


def checkRow(row, word):
    global matrix
    if isOutIndex(y=row) == True:
        return False
    for colMatrix in range(len(matrix[row])):
        countNotPossible = 0
        countThroughChar = 0
        colMatrixTemp = colMatrix

        for char in word:
            isOut = isOutIndex(row, colMatrixTemp)
            if(isOut):
                continue
            charMatrix = matrix[row][colMatrixTemp]
            if(charMatrix != char and charMatrix != ''):
                if len(charBefore) == 0:
                countNotPossible += 1
            if(charMatrix == char):
                countThroughChar += 1

            colMatrixTemp += 1
        print("kata {}, CNP = {}, CTC = {}".format(
            word, countNotPossible, countThroughChar))
        if(countNotPossible == 0 and countThroughChar > 0):
            return [row, colMatrix]
    return False


def checkColumn(column, word):
    global matrix
    if isOutIndex(x=column) == True:
        return False
    for rowMatrix in range(len(matrix)):
        countNotPossible = 0
        countThroughChar = 0
        rowMatrixTemp = rowMatrix
        for char in word:
            isOut = isOutIndex(rowMatrixTemp, column)
            if(isOut):
                continue
            charMatrix = matrix[rowMatrixTemp][column]
            if(charMatrix != char and charMatrix != ''):
                countNotPossible += 1
            if(charMatrix == char):
                countThroughChar += 1

            rowMatrixTemp += 1
        if(countNotPossible == 0 and countThroughChar > 0):
            return [rowMatrix, column]
    return False


def isOutIndex(x=0, y=0):
    global matrix
    if(x > len(matrix) - 1):
        return True
    if(y > len(matrix[x]) - 1):
        return True
    return False


def putToMatrix(word, wordStart, direction):
    print("masukkan kata {} di posisi {} dengan arah {}".format(
        word, wordStart, direction))
    global matrix
    posX = wordStart[0]
    posY = wordStart[1]

    for char in word:
        if(isOutIndex(posX)):
            matrix.append([])
        if(isOutIndex(posX, posY)):
            matrix[posX].append('')
        print("{}, {}".format(posX, posY))
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

    generateEmptyMatrix(10, 10)

    # Run First
    isFirst = True
    for word in words:
        if isFirst:
            putToMatrix(word, [0, 0], HORIZONTAL)
            isFirst = False
            continue
        print("coba kata {}".format(word))
        findPosition(word)

    print(DataFrame(matrix))
