from problems.firstCommonAncestor import firstCommonAncestor
from problems.checkSubtree import checkTree, _getTreeElements
from ds.binaryTree import LinkedBinaryTree, Node
from random import randint

if __name__ == '__main__':
  firstTree = LinkedBinaryTree()
  secondTree = LinkedBinaryTree()
  for i in range(20):
    if i < 15:
      firstTree.insert(Node(data=randint(1, 20)))
    else:
      secondTree.insert(Node(data=randint(21,40)))

  print(_getTreeElements(firstTree.getRoot()))
  print(_getTreeElements(secondTree.getRoot()))

  firstTree.insert(secondTree.getRoot())
  print(checkTree(firstTree.getRoot(), secondTree.getRoot()))
  # firstTree.insert(secondTree.getRoot())

  


