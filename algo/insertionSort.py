def insertionSortAsc(array: list):
  for curIndex in range(len(array)):
    cur = array[curIndex]
    prevIndex = curIndex - 1
    while (prevIndex >= 0 and array[prevIndex] > cur):
      array[prevIndex + 1] = array[prevIndex]
      prevIndex -= 1
    array[prevIndex + 1] = cur; 
  return array
