def _binarySearch(arr, startIndex, endIndex, val):
  if startIndex >= endIndex:
    return -1 
  else:
    mid = startIndex + (endIndex - startIndex) // 2

    if arr[mid] == val:
      return mid
    elif arr[mid] > val:
      return _binarySearch(arr, startIndex, mid - 1, val)
    else:
      return _binarySearch(arr, mid + 1, endIndex, val)

def binarySearch(arr, val):
  startIndex = 0
  endIndex = len(arr) - 1
  return _binarySearch(arr, startIndex, endIndex, val)


print(binarySearch([2,3,5,6,6,99], 99))
