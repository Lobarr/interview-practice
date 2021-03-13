# print("Hello")


def robotPaths(matrix):
    # to optimize on space, we can use given matrix to track paths instead of external bitmap structure

    numRows = 0
    numCols = 0
    bitmap = None

    if matrix:
        numRows = len(matrix)
        numCols = len(matrix[0])
        bitmap = [[False for _ in range(numCols)] for _ in range(numRows)]

    def traverse(curRowIndex, curColIndex, bitmap):
        # base cases

        # out of bounds
        if not (0 <= curRowIndex < numRows and 0 <= curColIndex < numCols):
            return

        # arrived at destination
        if (curRowIndex == numRows - 1 and curColIndex == numCols - 1):
            traverse.numPaths += 1
            return

        # arrive at where we've seen
        if bitmap[curRowIndex][curColIndex]:
            return

        # recursive cases

        bitmap[curRowIndex][curColIndex] = True

        traverse(curRowIndex - 1, curColIndex, bitmap)  # going up
        traverse(curRowIndex + 1, curColIndex, bitmap)  # going down
        traverse(curRowIndex, curColIndex - 1, bitmap)  # going left
        traverse(curRowIndex, curColIndex + 1, bitmap)  # going right

        bitmap[curRowIndex][curColIndex] = False

    traverse.numPaths = 0
    traverse(0, 0, bitmap)

    return traverse.numPaths


example1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
example1_solution = 38

example2 = [[0, 0, 0], [0, 0, 0]]
example2_solution = 4

example3 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
example3_solution = 7110272

print(robotPaths(example1) == example1_solution)
print(robotPaths(example2) == example2_solution)
print(robotPaths(example3) == example3_solution)

# my video has cut out; still frozen...; network on webcam computer is not connecting; will restart

# we noticed, hop back on when you can; should we try slack?; okay lmk
