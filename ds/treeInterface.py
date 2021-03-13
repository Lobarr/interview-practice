ERR_NOT_IMPLEMENTED = NotImplementedError('must be implemented by subclasses')


class Tree:
    """ 
  abstract base class representing a tree structure 
  """
    class Node:
        """
    an abstraction representing the location of a single element
    """
        def getElement(self):
            raise ERR_NOT_IMPLEMENTED

        def __eq__(self, check):
            raise ERR_NOT_IMPLEMENTED

        def __ne__(self, check):
            raise not (self == check)

    def root(self):
        raise ERR_NOT_IMPLEMENTED

    def parent(self, node):
        raise ERR_NOT_IMPLEMENTED

    def numChildren(self, node):
        raise ERR_NOT_IMPLEMENTED

    def children(self, node):
        raise ERR_NOT_IMPLEMENTED

    def __len__(self):
        raise ERR_NOT_IMPLEMENTED

    def isRoot(self, node):
        return self.root() == node

    def isLeaf(self, node):
        return self.numChildren(node) == 0

    def isEmpty(self):
        return len(self) == 0

    def depth(self, node):
        if self.isRoot(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

    def height(self, node):
        if self.isLeaf(node):
            return 0
        else:
            return 1 + max(self.height(child) for child in self.children(node))


class BinaryTree(Tree):
    def left(self, node):
        raise ERR_NOT_IMPLEMENTED

    def right(self, node):
        raise ERR_NOT_IMPLEMENTED

    def sibling(self, node):
        parent = self.parent(node)
        if not parent:
            return None
        else:
            return self.right(parent) if node == self.left(
                parent) else self.left(node)

    def children(self, node):
        if self.left(node) != None:
            yield self.left(node)

        if self.right(node) != None:
            yield self.right(node)
