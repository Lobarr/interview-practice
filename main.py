from problems.firstCommonAncestor import firstCommonAncestor
from ds.binaryTree import LinkedBinaryTree, Node

if __name__ == '__main__':
  tree = LinkedBinaryTree()
  for i in range(10):
    tree.insert(Node(data=i))

  firstNode = Node(data=20)
  secondNode = Node(data=-20)

  tree.insert(firstNode)
  tree.insert(secondNode)

  print(firstCommonAncestor(firstNode, secondNode))