from ds.binaryTree import LinkedBinaryTree, Node
from queue import Queue


def _getTreeElements(node: Node) -> list:
    elements = []
    queue = Queue()
    queue.put(node)

    while not queue.empty():
        cur: Node = queue.get()
        elements.append(cur.getData())
        for child in cur.getChildren():
            queue.put(child)

    return elements


def checkTree(firstTree: Node, secondTree: Node):
    if not firstTree or not secondTree:
        return False

    cur = firstTree
    foundSubtreeRoot: Node = None  # root of the secondTree found in the first tree

    while cur and not foundSubtreeRoot:
        if cur.getData() > secondTree.getData():
            cur = cur.getLeft()
        elif cur.getData() < secondTree.getData():
            cur = cur.getRight()
        else:
            foundSubtreeRoot = cur

    if not foundSubtreeRoot:
        return False

    if _getTreeElements(foundSubtreeRoot) != _getTreeElements(secondTree):
        return False

    return True
