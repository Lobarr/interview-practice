from ds.binaryTree import Node

def firstCommonAncestor(firstNode: Node, secondNode: Node):
  firstPathToRoot = _getPathtoRoot(firstNode)

  cur = secondNode
  while cur:
    curMemoryAddr = _getMemoryAddr(cur)
    if curMemoryAddr in firstPathToRoot:
      return cur
    cur = cur.getParent()

  return None

def _getMemoryAddr(node: Node):
  return hex(id(node))

def _getPathtoRoot(node: Node):
  path = {}
  cur = node
  while cur:
    path[_getMemoryAddr(cur)] = True
    cur = cur.getParent()
  return path
