def binarySearch(target: int, arr: list, lowIndex: int, highIndex: int):
    """
  binary search on a sorted array
  """
    if lowIndex > highIndex:
        return False
    else:
        mid = (lowIndex + highIndex) // 2
        if target < arr[mid]:
            return binarySearch(target, arr, lowIndex, mid - 1)
        elif target > arr[mid]:
            return binarySearch(target, arr, mid + 1, highIndex)
        else:
            return True
