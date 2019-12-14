def bubbleSort(arr):
  arrLength = len(arr) - 1
  for i in range(arrLength):
    swapped = False
    for j in range(arrLength - i):
      if arr[j] >= arr[j+1]:
        swapped = True
        arr[j], arr[j+1] = arr[j+1], arr[j]
    if swapped == False: break
  return arr
