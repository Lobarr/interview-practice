def insertionSortAsc(array: list):
  for curIndex in range(len(array)):
    cur = array[curIndex]
    prev = curIndex - 1
    while (prev >= 0 and array[prev] > cur):
      array[prev + 1] = array[prev]
      prev -= 1
    array[prev + 1] = cur; 
  return array
