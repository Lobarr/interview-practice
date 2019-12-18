class StackOfPlates:
  def __init__(self, stackLimit: int):
    self.stacks = []
    self.stackLimit = stackLimit

  def _isFull(self, stack: list):
    return len(stack) >= self.stackLimit      

  def push(self, data):
    if not self.stacks or self._isFull(self.stacks[-1]):
      print('creating new stack')
      newStack = []
      newStack.append(data)
      self.stacks.append(newStack)
    else:
      print('adding to last stack')
      self.stacks[-1].append(data)

  def isEmpty(self):
    return False if self.stacks else True

  def pop(self):
    print('removing last element from tail stack')
    if self.stacks:
      tailStack = self.stacks[-1]
      lastElement = tailStack.pop(-1)
      if not tailStack:
        print('removing empty stack')
        self.stacks.pop(-1)
      return lastElement
    return -1

  def popAt(self, index):
    if not (0 <= index < len(self.stacks)):
      raise Exception('invalid index provided')
    selectedStack = self.stacks[index]
    lastElement = selectedStack.pop(-1)
    if not selectedStack:
      self.stacks.pop(index)
    return lastElement

  
if __name__ == '__main__':
  stackofPlates = StackOfPlates(3)
  for i in range(9):
    stackofPlates.push(i)
    print(f'added element {i}')
  
  print('removing element from first stack', stackofPlates.popAt(0))
  while not stackofPlates.isEmpty():
    print(stackofPlates.pop())