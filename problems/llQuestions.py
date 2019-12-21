class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None
  
  def getData(self):
    return self.data

  def getNext(self):
    return self.next
  
  def setNext(self, next):
    self.next = next

  def isEmpty(self):
    return self.getData() == None and self.getNext()
  
def add(head: Node, data):
  newNode = Node(data) if not isinstance(data, Node) else data
  if not head or head.isEmpty():
    return newNode
  
  cursor = head
  while cursor.getNext() != None:
    cursor = cursor.getNext()
  cursor.setNext(newNode)

def printList(head: Node):
  if not head:
    return

  cursor = head
  while cursor != None:
    print(cursor.getData())
    cursor = cursor.getNext()

def removeDup(head: Node):
  if not head:
    return

  cur = head
  seen = { cur.getData(): True }
  
  while cur.getNext():
    if cur.getNext().getData() in seen:
      cur.setNext(cur.getNext().getNext())
    else:
      seen[cur.getData()] = True
    cur = cur.getNext()

def partition(head: Node, val: int):
  leftPartition = None
  rightPartition = None

  if not head:
    return

  cur = head
  while cur != None:
    if cur.getData() < val:
      if not leftPartition:
        leftPartition = Node(cur.getData())
      else:
        add(leftPartition, cur.getData())
    else:
      if not rightPartition:
        rightPartition = Node(cur.getData())
      else:
        add(rightPartition, cur.getData())
    cur = cur.getNext()

  cur = leftPartition
  while cur.getNext() != None:
    cur = cur.getNext()
  cur.setNext(rightPartition)
  return leftPartition


def sumLists(firstList: Node, secondList: Node):

  def parseValue(head: Node):
    stack = []
    value = ''

    cur = head
    while cur != None:
      if type(cur.getData()) != int:
        raise Exception('only supports adding int values')
      stack.append(cur.getData())
      cur = cur.getNext()

    while stack:
      value += str(stack.pop(-1))
    
    return int(value)

  return parseValue(firstList) + parseValue(secondList)

def isPalindrome(firstList: Node, secondList: Node):
  if not firstList or not secondList:
    raise Exception('unable to perform action on empty list')

  stack = []

  cur = firstList
  while cur != None:
    stack.append(cur.getData())
    cur = cur.getNext()

  cur = secondList
  while cur != None:
    if not stack or stack.pop(-1) != cur.getData():
      return False
    cur = cur.getNext()

  return True

def intersection(firstList: Node, secondList: Node):
  if not firstList or not secondList:
    raise Exception('unable to perform action on empty list')
    
  seenNodeRefs = {}
  cur = firstList
  while cur != None:
    nodeRef = hex(id(cur))
    if nodeRef not in seenNodeRefs:
      seenNodeRefs[nodeRef] = True
    cur = cur.getNext()

  cur = secondList
  while cur != None:
    nodeRef = hex(id(cur))
    if nodeRef in seenNodeRefs:
      return cur
    cur = cur.getNext()
  
  return None
  

def makeList(values: list):
  node = None
  for i in values:
    if not node:
      node = Node(i)
    else:
      add(node, i)
  return node

if __name__ == '__main__':
  firstList = Node(1)
  intersectingNode = Node(5)
  print('intersecting node ref ', hex(id(intersectingNode)))
  add(firstList, 2)
  add(firstList, 3)
  add(firstList, 4)
  add(firstList, intersectingNode)
  add(firstList, 6)

  secondList = Node(1)
  for i in range(2, 6):
    add(secondList, i)
  add(secondList, intersectingNode)

  print(intersection(firstList, secondList))
  # print(isPalindrome(firstList, secondList))