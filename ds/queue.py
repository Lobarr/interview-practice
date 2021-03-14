from ds.dLinkedList import DLinkedList

ERR_EMPTY_QUEUE = Exception('Queue has no elements')
ERR_INVALID_NODE = Exception('cannot update invalid node')


class DLLQueue:
    """
  queue data structure implemented using a double linked list
  """
    def __init__(self):
        self.linkedList = DLinkedList()

    def enqueue(self, data):
        self.linkedList.insertFront(data)

    def dequeue(self):
        return self.linkedList.removeBack()

    def getCount(self):
        return self.linkedList.getCount()

    def peek(self):
        linkedListTail = self.linkedList.getTail()
        return linkedListTail.data if linkedListTail else None

    def printAsc(self):
        self.linkedList.printListAsc()

    def printDes(self):
        self.linkedList.printListDes()


class Deque:
    def __init__(self, capacity=5):
        self.count = 0
        self.frontIndex = 0
        self.queue = [None] * capacity

    def insertFirst(self, data):
        if self.isFull():
            newCapacity = 2 * len(self.queue)
            self._resize(newCapacity)
        newFrontIndex = (self.frontIndex - 1) % len(self.queue)
        self.queue[newFrontIndex] = data
        self.frontIndex = newFrontIndex
        self.count += 1

    def insertLast(self, data):
        if self.isFull():
            newCapacity = 2 * len(self.queue)
            self._resize(newCapacity)
        nextIndex = (self.frontIndex + self.count) % len(self.queue)
        self.queue[nextIndex] = data
        self.count += 1

    def removeFirst(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        frontData = self.queue[self.frontIndex]
        self.queue[self.frontIndex] = None
        self.frontIndex = (self.frontIndex + 1) % len(self.queue)
        self.count -= 1
        return frontData

    def removeLast(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        backIndex = (self.frontIndex + self.count - 1) % len(self.queue)
        self.queue[backIndex] = None
        self.count -= 1

    def getFirstElement(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        return self.queue[self.frontIndex]

    def getLastElement(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        backIndex = (self.frontIndex + self.count - 1) % len(self.queue)
        return self.queue[backIndex]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)

    def __len__(self):
        return self.count

    def _resize(self, newCapacity):
        oldQueue = self.queue
        frontIndex = self.frontIndex
        self.queue = [None] * newCapacity
        for i in range(self.count):
            self.queue[i] = oldQueue[frontIndex]
            frontIndex = (frontIndex + 1) % len(oldQueue)
        self.frontIndex = 0

    def printQueue(self):
        frontIndex = self.frontIndex
        for i in range(self.count):
            print(self.queue[frontIndex])
            frontIndex = (frontIndex + 1) % len(self.queue)
        print('\n')


class ArrayQueue:
    """
  queue data structure implemented using a circular array
  """
    def __init__(self, capacity=5):
        self.count = 0
        self.frontIndex = 0
        self.queue = [None] * capacity

    def enqueue(self, data):
        if self.isFull():
            newCapacity = 2 * len(self.queue)
            self._resize(newCapacity)
        nextIndex = (self.frontIndex + self.count) % len(self.queue)
        self.queue[nextIndex] = data
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        frontData = self.queue[self.frontIndex]
        self.queue[self.frontIndex] = None
        self.frontIndex = (self.frontIndex + 1) % len(self.queue)
        self.count -= 1
        return frontData

    def __len__(self):
        return self.count

    def getFirstElement(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        return self.queue[self.frontIndex]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)

    def _resize(self, newCapacity):
        oldQueue = self.queue
        frontIndex = self.frontIndex
        self.queue = [None] * newCapacity
        for i in range(self.count):
            self.queue[i] = oldQueue[frontIndex]
            frontIndex = (frontIndex + 1) % len(oldQueue)
        self.frontIndex = 0

    def printQueue(self):
        frontIndex = self.frontIndex
        for i in range(self.count):
            print(self.queue[frontIndex])
            frontIndex = (frontIndex + 1) % len(self.queue)
        print('\n')


class PNode:
    def __init__(self, priority: int, data):
        self.priority = priority
        self.data = data
        self._index = None

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def _setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def __lt__(self, check):
        return self.getPriority() < check.getPriority()

    def __eq__(self, check):
        return (self.getData() == check.getData()
                and self.getPriority() == check.getPriority()
                and self.getIndex() == check.getIndex())


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.count = 0

    def getParentIndex(self, index: int):
        parentIndex = (index - 1) // 2
        return parentIndex if parentIndex <= self.count else None

    def getLeftNodeIndex(self, index: int):
        leftNodeIndex = (index * 2) + 1
        return leftNodeIndex if leftNodeIndex <= self.count else None

    def getRightNodeIndex(self, index: int):
        rightNodeIndex = (index * 2) + 2
        return rightNodeIndex if rightNodeIndex <= self.count else None

    def isEmpty(self):
        return len(self.queue) == 0

    def getCount(self):
        return len(self.queue)

    def enqueue(self, node: PNode):
        nextIndex = len(self.queue)
        node._setIndex(nextIndex)
        self.queue.append(node)
        self.bubbleUp(nextIndex)
        return node

    def peek(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        return self.queue[0]

    def dequeue(self):
        if self.isEmpty():
            raise ERR_EMPTY_QUEUE
        lastNodeIndex = self.getCount() - 1
        self.swap(0, lastNodeIndex)
        item = self.queue.pop()
        self.bubbleDown(0)
        return item

    def swap(self, fromIndex: int, toIndex: int):
        self.queue[fromIndex], self.queue[toIndex] = self.queue[
            toIndex], self.queue[fromIndex]

    def verifyNode(self, node: PNode):
        return (0 <= node.getIndex() < self.getCount()
                and self.queue[node.getIndex()] is node)

    def update(self, node: PNode, newNode: PNode):
        if not self.verifyNode(node):
            raise ERR_INVALID_NODE
        node.setData(newNode.getData())
        node.setPriority(newNode.getPriority())
        self.bubble(node.getIndex())

    def remove(self, node: PNode):
        if not self.verifyNode(node):
            raise ERR_INVALID_NODE
        lastIndex = self.getCount() - 1
        if node.getIndex() == lastIndex:
            self.queue.pop()
        else:
            self.swap(node.getIndex(), lastIndex)
            self.queue.pop()
            self.bubble(node.getIndex())

    def heapify(self):
        """
    bottom up heap construction - given queue is filled with leaf nodes
    """
        lastLeafIndex = self.getCount() - 1
        start = self.getParentIndex(lastLeafIndex)
        for i in range(start, -1, -1):
            self.bubble(i)

    def bubble(self, index):
        if (index > 0 and index <= self.getCount() - 1 and
                self.queue[index] < self.queue[self.getParentIndex(index)]):
            self.bubbleUp(index)
        else:
            self.bubbleDown(index)

    def bubbleUp(self, index):
        parentIndex = self.getParentIndex(index)
        if (parentIndex != None and index > 0
                and self.queue[index] < self.queue[parentIndex]):
            self.swap(index, parentIndex)
            self.bubbleUp(parentIndex)

    def bubbleDown(self, index):
        if 0 < index < self.getCount() - 1:
            leftChildNodeIndex = self.getLeftNodeIndex(index)
            rightChildNodeIndex = self.getRightNodeIndex(index)
            smallerChildIndex = None

            if leftChildNodeIndex != None:
                smallerChildIndex = leftChildNodeIndex

            if (rightChildNodeIndex != None and self.queue[rightChildNodeIndex]
                    < self.queue[leftChildNodeIndex]):
                smallerChildIndex = rightChildNodeIndex

            if self.queue[index] < self.queue[smallerChildIndex]:
                self.swap(index, smallerChildIndex)
