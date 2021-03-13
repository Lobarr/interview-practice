def search2DMatrix(matrix, target):

    # uses decrease and conquer to determine potential row
    def binarySearchRow(_matrix, _target):
        start = 0
        end = len(_matrix) - 1

        while start <= end:
            mid = start + (end - start) // 2
            row = _matrix[mid]

            if row[0] <= _target <= row[-1]:
                return row

            if row[0] > _target:
                end = mid - 1
            elif row[0] < _target:
                start = mid + 1

        return None

    # uses binary seaarch to find target
    def binarySearch(arr, _target):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] > _target:
                end = mid - 1
            elif arr[mid] < _target:
                start = mid + 1
            else:
                return True

        return False

    potentialRow = binarySearchRow(matrix, target)
    return binarySearch(potentialRow, target) if potentialRow else False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

print(search2DMatrix(matrix, 16) == True)
print(search2DMatrix(matrix, 3) == True)
print(search2DMatrix(matrix, 100) == False)
