matrix_3x3 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix_4x4 = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
]

matrix_5x5 = [
  [1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15],
  [16,17,18,19,20]
]

matrix_1x3 = [
  [1],
  [2],
  [3]
]

def spiralMatrix(matrix: list):
  print('starting')
  spiral = []
  while matrix:
    # get first row
    firstRow = matrix[0]
    print('first row ', firstRow)
    spiral += firstRow
    matrix.remove(firstRow)

    # get last column
    lastColumn = []
    for index, row in enumerate(matrix):
      lastColumn.append(row[-1])
      del matrix[index][-1]
      if not matrix[index]:
        del matrix[index]
    spiral += lastColumn
    print('last column ', lastColumn)

    #get last row
    if matrix:
      lastRow = matrix[-1]
      matrix.remove(lastRow)
      spiral += lastRow[::-1]
      print('last row ', lastRow)

    #get first column
    firstColumn = []
    for index, row in enumerate(matrix):
      firstColumn.append(row[0])
      del matrix[index][0]
    spiral += firstColumn[::-1]
    print('first column', firstColumn)

  return spiral
