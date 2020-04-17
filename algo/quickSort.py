def quickSort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    less, more = [], []

    for val in arr:
      if val <= pivot:
        less.append(val)
      else:
        more.append(val)

    return quickSort(less) + [pivot] + quickSort(more)