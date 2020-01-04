# def mergeSort(arr):
#   start = []
#   end = []
#   while len(arr) > 1:
#     minItem = min(arr)
#     maxItem = max(arr)
#     start.append(minItem)
#     end.append(maxItem)
#     arr.remove(minItem)
#     arr.remove(maxItem)
#   end.reverse()
#   return (start + arr + end)



def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  firstHalf = mergeSort(arr[:mid])
  secondHalf = mergeSort(arr[mid:])
  return merge(firstHalf, secondHalf)

def merge(firstHalf, secondHalf):
  result = []
  while firstHalf and secondHalf:
    next = (firstHalf if firstHalf[0] <= secondHalf[0] else secondHalf).pop(0)
    result.append(next)
  return result + firstHalf + secondHalf