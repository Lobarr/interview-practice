def mergeSort(arr):
  start = []
  end = []
  while len(arr) > 1:
    minItem = min(arr)
    maxItem = max(arr)
    start.append(minItem)
    end.append(maxItem)
    arr.remove(minItem)
    arr.remove(maxItem)
  end.reverse()
  return (start + arr + end)