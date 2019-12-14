from ds.queue import ArrayQueue

ERR_TREE_NOT_EMPTY = Exception('Tree is not empty')
ERR_TREE_EMPTY = Exception('Tree is empty')

class Node:
  def __init__(self, parent = None, left = None, right = None, data = None):
    self._parent = parent
    self._left = left
    self._right = right
    self._data = data
    self._key = None
    self._value = None

  def getKey(self):
    return self._key

  def setKey(self, key):
    self._key = key

  def getValue(self):
    return self._value

  def setValue(self, value):
    self._value = value

  def getLeft(self):
    return self._left

  def setLeft(self, left):
    self._left = left

  def getRight(self):
    return self._right

  def setRight(self, right):
    self._right = right

  def getParent(self):
    return self._parent

  def setParent(self, parent):
    self._parent = parent

  def getData(self):
    return self._data

  def setData(self, data):
    self._data = data

  def isRoot(self):
    return self._parent == None

  def hasChildren(self):
    return (
      self._left != None 
      or self._right != None
    )

  def numChildren(self):
    count = 0
    if self._left != None:
      count += 1
    if self._right != None:
      count += 1
    return count

  def isLeaf(self):
    return (
      not self.hasChildren() 
      and self._parent != None
    )

  def isEmpty(self):
    return (
      not self.hasChildren() 
      and self.getParent() == None
      and self.getData() == None
    )

  def getChildren(self):
    if self._left != None:
      yield self._left
    if self._right != None:
      yield self._right
  
  def __eq__(self, check):
    return (
      check.getLeft() == self.getLeft()
      and check.getRight() == self.getRight()
      and check.getData() == self.getData()
      and self.getParent() == check.getParent()
    )

class LinkedBinaryTree:
  def __init__(self):
    self._root: Node = None
    self._size = 0

  def getRoot(self):
    return self._root

  def setRoot(self, node):
    if not self.isEmpty():
      raise ERR_TREE_NOT_EMPTY
    self._root = node
    self._size = 1
  
  def isRoot(self, node):
    return self._root == node

  def isEmpty(self):
    return self._root == None

  def getNode(self, data):
    cur = self.getRoot()
    while cur != None:
      if data > cur.getData():
        cur = cur.getRight()
      elif data < cur.getData():
        cur = cur.getLeft()
      else:
        return cur
    return None

  def depth(self, node: Node):
    if self.isRoot(node):
      return 0
    else:
      return 1 + self.depth(node.getParent())

  def height(self, node: Node):
    if node.isLeaf():
      return 0
    else:
      return 1 + max(self.height(child) for child in node.getChildren())

  def remove(self, node: Node):
    if node.numChildren() > 1:
      raise Exception('unable to remove node with more than 1 child')
      
    parent = node.getParent()
    selectedChild = node.getLeft() if not node.getRight() else node.getRight()
    selectedChild and selectedChild.setParent(parent)
    if node == self.getRoot():
      self._root = selectedChild
    else:
      if node == parent.getRight():
        parent.setRight(selectedChild)
      else:
        parent.setLeft(selectedChild)
    self._size -= 1

  def preOrderTraversal(self):
    self._preOrderTraversal(self.getRoot())

  def inOrderTraversal(self):
    self._inOrderTraversal(self.getRoot())

  def postOrderTraversal(self):
    self._postOrderTraversal(self.getRoot())
  
  def _preOrderTraversal(self, node: Node):
    if node:
      print(node.getData())
      for child in node.getChildren():
        self._preOrderTraversal(child)

  def _inOrderTraversal(self, node: Node):
    if node:
      self._inOrderTraversal(node.getLeft())
      print(node.getData())
      self._inOrderTraversal(node.getRight())

  def _postOrderTraversal(self, node: Node):
    if node:
      for child in node.getChildren():
        self._postOrderTraversal(child)
      print(node.getData())

  def _breadthFirstTraversal(self, node: Node):
    queue = ArrayQueue()
    queue.enqueue(node)
    while not queue.isEmpty():
      curNode = queue.dequeue()
      print(curNode.getData())
      for child in curNode.getChildren():
        queue.enqueue(child)

  def _depthFirstTraversal(self, node: Node):
    pass

  def _eulerTourTraversal(self, node: Node):
    if node:
      self.preVisitHook(node)
      for child in node.getChildren():
        self._eulerTourTraversal(child)
      self.postVisitHook(node)

  def preVisitHook(self, node: Node):
    """
    some computation
    """
    pass
  
  def postVisitHook(self, node: Node):
    """
    some computation
    """
    pass
  
  def insert(self, node: Node):
    if self.isEmpty():
      self.setRoot(node)
    else: 
      cur = self.getRoot()
      while True:
        if node.getData() > cur.getData():
          if not cur.getRight():
            node.setParent(cur)
            cur.setRight(node)
            break
          cur = cur.getRight()
        else:
          if not cur.getLeft():
            node.setParent(cur)
            cur.setLeft(node)
            break
          cur = cur.getLeft()
        self._size += 1

  def _subtreeSearch(self, node: Node, key):
    if key == node.getKey():
      return node
    elif key < node.getKey():
      if node.getLeft() != None:
        return self._subtreeSearch(node.getLeft(), key)
    else:
      if node.getRight() != None:
        return self._subtreeSearch(node.getRight(), key)
    return node # returns last node seen if not found

  def _subtreeFirstPosition(self, node: Node):
    walk = node.getLeft()
    while walk != None:
      walk = node.getLeft()
    return walk

  def _subtreeLastPosition(self, node: Node):
    walk = node.getRight()
    while walk != None:
      walk = node.getRight()
    return walk

  def first(self):
    return self._subtreeFirstPosition(self.getRoot()) if not self.isEmpty() else None

  def last(self):
    return self._subtreeLastPosition(self.getRoot()) if not self.isEmpty() else None

  def after(self, node: Node):
    if node:
      if node.getRight() != None:
        # successor is leftmost position in p's right subtree
        return self._subtreeFirstPosition(node.getRight())
      else:
        # successor is nearest ancestor having p in it's left subtree
        walk = node
        ancestor = node.getParent()
        while (
          ancestor != None
          and walk == ancestor.getRight()
        ):
          walk = ancestor
          ancestor = walk.getParent()
        return ancestor

  def before(self, node: Node):
    if node:
      if node.getLeft() != None:
        return self._subtreeLastPosition(node.getLeft())
      else:
        walk = node
        ancestor = node.getParent()
        while (
          ancestor != None
          and walk == ancestor.getLeft()
        ):
          walk = ancestor
          ancestor = walk.getParent()
        return ancestor

  def findPosition(self, key):
    if self.isEmpty():
      raise ERR_TREE_NOT_EMPTY
    node = self._subtreeSearch(self.getRoot(), key)
    return node

  def findMin(self):
    return self.first()

  def findMax(self):
    return self.last()

  def findGreaterOrEqual(self, key):
    if self.isEmpty():
      return None
    else:
      node = self.findPosition(key)
      if node.getKey() < key:
        node = self.after(node)
      return node

  def findRange(self, startKey, stopKey):
    if not self.isEmpty():
      items = []
      node = self.findPosition(startKey)
      if node.getKey() < startKey:
        node = self.after(node)
      while (
        node != None
        and (stopKey == None or node.getKey() < stopKey)
      ):
        items.append(node)
        node = self.after(node)
      return items

  def getKey(self, key):
    if self.isEmpty():
      raise ERR_TREE_EMPTY
    else:
      node = self._subtreeSearch(key)
      if node.getKey() != key:
        raise KeyError()
      return node.getValue()

  def _makeNode(self, key, value):
    newNode = Node()
    newNode.setKey(key)
    newNode.setValue(value)
    return newNode

  def setKey(self, key, value):
    if self.isEmpty():
      self.setRoot(self._makeNode(key, value))
    else:
      node = self._subtreeSearch(key)
      if node.getKey() != key:
        if node.getKey() < key:
          node.setLeft(self._makeNode(key, value))
        else:
          node.setRight(self._makeNode(key, value))
      else:
        node.setValue(value)

  def _replace(self, fromNode: Node, toNode: Node):
    toNode.setParent(fromNode.setParent())
    toNode.setLeft(fromNode.getLeft())
    toNode.setRight(fromNode.getRight())

    if fromNode.getLeft():
      leftChild = fromNode.getLeft()
      leftChild.setParent(toNode)

    if fromNode.getRight():
      rightChild = fromNode.getRight()
      rightChild.setParent(toNode)
    
  def delete(self, node: Node):
    if node.getRight() and node.getLeft():
      # replace node with rightmost leaf node in the left subtree
      replacementNode = self._subtreeLastPosition(node.getLeft())
      self._replace(node, replacementNode)
      return
    
    if node.getRight():
      self._replace(node, node.getRight())

    if node.getLeft():
      self._replace(node, node.getLeft())
  
  def _relink(self, parentNode: Node, childNode: Node, makeLeftChild: bool = True):
    if makeLeftChild:
      parentNode.setLeft(childNode)
    else:
      parentNode.setRight(childNode)

    if childNode != None:
      childNode.setParent(parentNode)

  def _rotate(self, node: Node):
    """
    rotates node above it's parent
    """
    parent = node.getParent()
    grandParent = parent.getParent()

    if not grandParent:
      self.setRoot(node)
      node.setParent(None)
    else:
      self._relink(grandParent, node, parent == grandParent.getLeft()) # bump child (node) above it's parent
    
    if node == parent.getLeft():
      self._relink(parent, node.getRight(), True) # since node's right side is less than parent
      self._relink(node, parent, False) # since parent is greater than child
    else:
      self._relink(parent, node.getLeft(), False) # since node's left side is greater than parent
      self._relink(node, parent, True)

  def _restructure(self, node: Node):
    """
    performs tri-node restructuring
    """
    parent = node.getParent()
    grandParent = parent.getParent()
    if (
      node == parent.getRight()
      and parent == grandParent.getRight()
    ):
      self._rotate(parent)
      return parent
    else:
      self._rotate(node)
      self._rotate(node)
      return node
  
class ArrayBinaryTree:
  def __init__(self, numLevels = 2):
    self.data = []

  def isEmpty(self):
    return len(self.data) == 0

  def getLeftChild(self, index):
    return (index * 2) + 1

  def getRightChild(self, index):
    return (index * 2) + 2

  def getParent(self, index):
    return (index - 1) // 2


# class ExpressionTree:
#   TOKENS = '/*+-'
#   def __init__(self, token: str):
#     if token not in ExpressionTree.TOKENS or len(token) > 1:
#       raise Exception('unsupported operation provided')
#     self._root = Node().setData(token)
  
#   def getRoot(self):
#     return self._root

#   def setRoot(self, node: Node):
#     if self.getRoot() != None:
#       raise Exception(ERR_TREE_NOT_EMPTY)
#     self._root = node

#   def isEmpty(self):
#     return self.getRoot() is None

#   def addOperation(self, operation, leftSide, rightSide):
#     newNode = Node(None, leftSide, rightSide, operation)
#     cur = self.getRoot()
#     while True:
#       if cur.getLeft() == None:
#         newNode.setParent(cur)
#         cur.setLeft(newNode)
#         break
      
        