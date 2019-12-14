from ds.dLinkedList import DLinkedList

class Position:
  def __init__(self, data  = None):
    self.data = data
  
  def setData(self, data):
    self.data = data
  
  def getData(self):
    return self.data

class PositionList:
  def __init__(self):
    self.list = DLinkedList()
    self.front = None
    self.back = None
  
  def isEmpty(self):
    return self.front == self.back == None

  def getFront(self):
    return self.front

  def getBack(self):
    return self.back

  def addFront(self, data):
    newFront = Position(data)
    self.list.insertFront(newFront)
    self.front = newFront

  def setBack(self, data):
    newBack = Position(data)
    self.list.insertBack(newBack)
    self.back = newBack

  def addBefore(self, position,  data):
    pass
  
  def addAfter(self, position, data):
    pass

  def replace(self, position, data):
    pass
    
  def remove(self, position):
    pass