def sortStack(stack: list):
  sortedStack = []

  while stack:
    nextValue = stack.pop(-1)
    if not sortedStack:
      sortedStack.append(nextValue)
    else:
      if nextValue <= sortedStack[-1]:
        sortedStack.append(nextValue)
      else:
        while sortedStack and nextValue > sortedStack[-1]:
          stack.append(sortedStack.pop(-1))
        sortedStack.append(nextValue)
  
  return sortedStack


if __name__ == '__main__':
  stack = [5,4,1,0,2,8,9]
  print(stack)
  print(sortStack(stack))