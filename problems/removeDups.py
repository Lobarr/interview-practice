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
  newNode = Node(data)
  if not head or head.isEmpty():
    return newNode
  
  cursor = head
  while cursor.getNext() != None:
    cursor = cursor.getNext()
  cursor.setNext(newNode)

def printList(head: Node):
  if not head:
    raise Exception('cant print empty list')

  cursor = head
  while cursor != None:
    print(cursor.getData())
    cursor = cursor.getNext()

def removeDup(head: Node):
  if not head:
    raise Exception('unable to perform action on empty list')

  cur = head
  seen = { cur.getData(): True }
  
  while cur.getNext():
    if cur.getNext().getData() in seen:
      cur.setNext(cur.getNext().getNext())
    else:
      seen[cur.getData()] = True
    cur = cur.getNext()

if __name__ == '__main__':
  head = Node(1)
  # print(head.getData())
  add(head, 2)
  add(head, 2)
  add(head, 2)
  add(head, 3)
  add(head, 4)
  add(head, 4)
  add(head, 4)
  add(head, 4)
  add(head, 4)
  printList(head)
  print()
  removeDup(head)
  printList(head)