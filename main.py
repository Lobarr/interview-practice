from queue import Queue
from pprint import pprint
from random import randint
from ds.sLinkedList import SLinkedList
from ds.binaryTree import LinkedBinaryTree, Node

def listOfDepths(tree: LinkedBinaryTree):
  if tree.isEmpty():
    return None

  depths = {}
  queue = Queue()
  queue.put((tree.getRoot(), 0))

  while not queue.empty():
    cur, depth = queue.get()
    if depth not in depths:
      depth_list = [cur]
      depths[depth] = depth_list
    else:
      depths[depth].append(cur)
    
    for child in cur.getChildren():
      queue.put((child, depth + 1))
    
  return depths

if __name__ == '__main__':
  tree = LinkedBinaryTree()
  for i in range(20):
    newNode = Node(data=randint(1, 100))
    tree.insert(newNode)

  depths = listOfDepths(tree)
  pprint(depths)