class SNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class SLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head is None

    def getNodeAtIndex(self, index):
        if not 0 <= index <= self.count - 1:
            raise Exception('invalid index passed in')
        curNode = self.head
        curIndex = 0
        while curNode != None:
            if curIndex == index:
                return curNode
            curNode = curNode.nextNode
            curIndex = curIndex + 1
        return None

    def search(self, data):
        curNode = self.head
        while curNode != None:
            if curNode.data == data:
                return curNode
            curNode = curNode.nextNode
        return None

    def printListAsc(self):
        curNode = self.head
        while curNode != None:
            print(curNode.data)
            curNode = curNode.nextNode

    def printListDes(self):
        def _helper(node: SNode):
            if not node:
                return

            if node.nextNode:
                _helper(node.nextNode)

            print(node.data)
            return

        _helper(self.head)

    def insertFront(self, data):
        self.insertAt(0, data)

    def insertBack(self, data):
        self.insertAt(self.count, data)

    def insertAt(self, index, data):
        if not 0 <= index <= self.count:
            raise Exception('invalid index provided')

        newNode = SNode(data)

        if self.head == None:
            self.head = newNode
        else:
            curNode = self.head
            prevNode = None
            curIndex = 0
            foundIndex = False

            while curNode != None:
                if curIndex == index:
                    foundIndex = True
                    newNode.nextNode = curNode

                    if prevNode:
                        prevNode.nextNode = newNode

                    if curIndex == 0:
                        self.head = newNode

                    break

                prevNode = curNode
                curNode = curNode.nextNode
                curIndex += 1

            if not foundIndex and index == self.count:
                prevNode.nextNode = newNode

        self.count += 1

    def removeFront(self):
        self.removeAt(0)

    def removeBack(self):
        self.removeAt(self.count - 1)

    def removeAt(self, index):
        curNode = self.head
        curIndex = 0
        prevNode = None
        while curNode != None:
            if curIndex == index:
                if prevNode != None:
                    prevNode.nextNode = curNode.nextNode
                else:
                    self.head = curNode.nextNode
                break
            prevNode = curNode
            curNode = curNode.nextNode
            curIndex += 1

        self.count -= 1

    def empty(self):
        while self.head != None:
            self.removeFront()

    def getHead(self):
        return self.head

    def bubbleSortAsc(self):
        if self.isEmpty():
            return

        endNode = None  # goes through entire list first
        while endNode != self.head.nextNode:
            curNode = self.head
            while curNode.nextNode != endNode:
                nextNode = curNode.nextNode
                if curNode.data > nextNode.data:
                    curNode.data, nextNode.data = nextNode.data, curNode.data
                curNode = curNode.nextNode
            endNode = curNode

    def bubbleSortDes(self):
        if self.isEmpty():
            return

        endNode = None
        while endNode != self.head.nextNode:
            curNode = self.head
            while curNode.nextNode != endNode:
                nextNode = curNode.nextNode
                if curNode.data < nextNode.data:
                    curNode.data, nextNode.data = nextNode.data, curNode.data
                curNode = curNode.nextNode
            endNode = curNode

    def reverse(self):
        if self.isEmpty():
            return

        curNode = self.head
        prevNode = None

        while curNode != None:
            nextNode = curNode.nextNode
            curNode.nextNode = prevNode
            prevNode = curNode
            curNode = nextNode

        self.head = prevNode # head node becomes last node

    def getCount(self):
        return self.count
