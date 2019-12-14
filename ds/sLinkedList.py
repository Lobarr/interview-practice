class SNode:
  def __init__(self, data, nextNode=None):
    self.data = data
    self.nextNode = nextNode

class SLinkedList:
  def __init__(self):
    self.head = None
    self.count = 0

  def isEmpty(self):
    return self.head == None

  def getNodeAtIndex(self, index):
    if not 0 <= index <= self.count - 1:
      raise Exception('invalid index passed in')
    curNode = self.head
    curIndex = self.count - 1
    while curNode != None:
      if curIndex == index:
        return curNode
      curNode = curNode.nextNode
      curIndex = curIndex + 1
  
  def search(self, data):
    curNode = self.head
    while curNode != None:
      if curNode.data == data:
        return curNode
      curNode = curNode.nextNode
    return None
  
  def printListAsc(self):
    curNode = self.head
    while curNode != None:
      print(curNode.data)
      curNode = curNode.nextNode
  
  def printListDes(self):
    nodes = []
    curNode = self.head
    while curNode != None:
      nodes.append(curNode)
      curNode = curNode.nextNode
    
    for _ in range(len(nodes)):
      print(nodes.pop().data)
  
  def insertFront(self, data):
    newNode = SNode(data)
    newNode.nextNode = self.head
    self.head = newNode
    self.count += 1

  def insertBack(self, data):
    newNode = SNode(data)
    if self.head == None:
      self.head = newNode
    else:
      curNode = self.head
      while curNode.nextNode != None:
        curNode = curNode.nextNode
      curNode.nextNode = newNode
    self.count += 1
  
  def insertAt(self, index, data):
    if not 0 <= index <= self.count - 1:
      raise Exception('invalid index provided')
    newNode = SNode(data)
    if self.head == None:
      self.head = newNode
    else:
      curNode = self.head
      curIndex = self.count - 1
      while curNode != None:
        if curIndex == index:
          newNode.nextNode = curNode.nextNode
          curNode.nextNode = newNode
          self.count += 1
        curNode = curNode.nextNode
        curIndex -= 1
    self.count += 1
  
  def removeFront(self):
    head = self.head
    if self.head != None:
      self.head = head.nextNode
      self.count -= 1
    return head
  
  def removeBack(self):
    curNode = self.head
    prevNode = None
    while curNode.nextNode != None:
      prevNode = curNode
      curNode = curNode.nextNode 
    prevNode.nextNode = None
    self.count -= 1
    return curNode
  
  def removeAt(self, index):
    curNode = self.head
    curIndex = self.count - 1
    prevNode = None
    while curNode != None:
      if curIndex == index:
        if prevNode != None:
          prevNode.nextNode = curNode.nextNode
        else:
          self.head = curNode.nextNode
      prevNode = curNode
      curNode = curNode.nextNode
      curIndex -= 1
      self.count -= 1

  def empty(self):
    while self.head != None:
      self.removeFront()

  def getHead(self):
    return self.head
    
  # def bubbleSortAsc(self):
  #   endNode = None # goes through entire list first
  #   while endNode != self.head.nextNode:
  #     curNode = self.head
  #     while curNode.nextNode != endNode:
  #       nextNode = curNode.nextNode
  #       if curNode.data > nextNode.data:
  #         curNode.data, nextNode.data = nextNode.data, curNode.data
  #       curNode = curNode.nextNode
  #     endNode = curNode
  
  # def bubbleSortDes(self):
  #   endNode = None
  #   while endNode != self.head.nextNode:
  #     curNode = self.head
  #     while curNode.nextNode != endNode:
  #       nextNode = curNode.nextNode
  #       if curNode.data < nextNode.data:
  #         curNode.data, nextNode.data = nextNode.data, curNode.data
  #       curNode = curNode.nextNode
  #     endNode = curNode
  
  def reverse(self):
    nodes = []
    while self.head != None:
      nodes.append(self.removeFront())
    for node in nodes:
      self.insertFront(node.data)

  def getCount(self):
    return self.count