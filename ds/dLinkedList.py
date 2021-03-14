class DNode:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None


class DLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None and self.tail == None

    def printListAsc(self):
        curNode = self.tail
        while curNode != None:
            print(curNode.data)
            curNode = curNode.prevNode

    def printListDes(self):
        curNode = self.head
        while curNode != None:
            print(curNode.data)
            curNode = curNode.nextNode

    def insertFront(self, data):
        newNode = DNode(data)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            curNode = self.head
            newNode.nextNode = curNode
            curNode.prevNode = newNode
            self.head = newNode
        self.count += 1

    def insertBack(self, data):
        newNode = DNode(data)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            curNode = self.tail
            newNode.prevNode = curNode
            curNode.nextNode = newNode
            self.tail = newNode
        self.count += 1

    def removeFront(self):
        curNode = self.head
        self.head = curNode.nextNode
        self.count -= 1
        return curNode

    def removeBack(self):
        curNode = self.tail
        self.tail = curNode.prevNode
        self.count -= 1
        return curNode

    def removeNode(self, node):
        prevNode = node.prevNode
        nextNode = node.nextNode
        if prevNode:
            prevNode.nextNode = nextNode
        else:
            self.head = nextNode
        if nextNode:
            nextNode.prevNode = prevNode
        else:
            self.tail = prevNode

    def removeAt(self, index):
        if not 0 <= index <= self.count:
            raise Exception('invalid index provided')
        if (index < self.count / 2):
            curIndex = 0
            curNode = self.tail
            while curNode != None:
                if index == curIndex:
                    self.removeNode(curNode)
                curNode = curNode.prevNode
                curIndex += 1
        else:
            curIndex = self.count - 1
            curNode = self.head
            while curNode != None:
                if index == curIndex:
                    self.removeNode(curNode)
                curNode = curNode.nextNode
                curIndex -= 1
        self.count -= 1

    def reverse(self):
        nodes = []
        while self.head != None:
            nodes.append(self.removeFront())
        for node in nodes:
            self.insertFront(node.data)

    # def bubbleSortAsc(self):
    #   end = None
    #   while end != self.head.nextNode:
    #     p = self.head
    #     while p.nextNode != end:
    #       q = p.nextNode
    #       if p.data > q.data:
    #         p.data, q.data = q.data, p.data
    #       p = p.nextNode
    #     end = p

    # def bubbleSortDes(self):
    #   end = None
    #   while end != self.head.nextNode:
    #     p = self.head
    #     while p.nextNode != end:
    #       q = p.nextNode
    #       if p.data < q.data:
    #         p.data, q.data = q.data, p.data
    #       p = p.nextNode
    #     end = p

    def insertAt(self, index, data):
        newNode = DNode(data)
        curNode = self.head
        curIndex = self.count - 1
        while curNode != None:
            if curIndex == index:
                newNode.nextNode = curNode.nextNode
                newNode.prevNode = curNode
                curNode.nextNode = newNode
                self.count += 1
            curNode = curNode.nextNode
            curIndex -= 1

    def empty(self):
        while not self.isEmpty():
            self.removeFront()

    def getCount(self):
        return self.count

    def getTail(self):
        return self.tail

    def getHead(self):
        return self.head

    def getNodeAtIndex(self, index):
        if not 0 <= index <= self.count - 1:
            raise ('invalid index passed in')
        curNode = self.head
        curIndex = self.count - 1
        while curNode != None:
            if curIndex == index:
                return curNode
            curNode = curNode.nextNode
            curIndex -= 1
        return None
