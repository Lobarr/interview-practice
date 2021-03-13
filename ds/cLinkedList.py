class CNode:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class CLinkedList:
    def __init__(self):
        self.cursor = CNode(None)
        self.count = 0

    def isEmpty(self):
        return self.cursor.nextNode == None

    def empty(self):
        for _ in range(self.count):
            self.remove()

    def printListAsc(self):
        curNode = self.cursor.nextNode
        while curNode != self.cursor:
            print(curNode.data)
            curNode = curNode.nextNode

    def printListDes(self):
        nodes = []
        curNode = self.cursor.nextNode
        while curNode != self.cursor:
            nodes.append(curNode)
            curNode = curNode.nextNode
        for _ in range(len(nodes)):
            print(nodes.pop().data)

    def insert(self, data):
        newNode = CNode(data)
        if self.isEmpty():
            newNode.nextNode = self.cursor
            self.cursor.nextNode = newNode
        else:
            newNode.nextNode = self.cursor.nextNode
            self.cursor.nextNode = newNode
        self.count += 1

    def remove(self):
        if self.isEmpty() == False:
            curNode = self.cursor.nextNode
            if curNode == self.cursor:
                self.cursor.nextNode = None
            else:
                self.cursor.nextNode = curNode.nextNode
            self.count -= 1
            return curNode

    def getNodeAtIndex(self, index):
        if 0 <= index <= self.count - 1:
            curNode = self.cursor.nextNode
            curIndex = self.count - 1
            while curNode != self.cursor:
                if curIndex == index:
                    return curNode
                curNode = curNode.nextNode
                curIndex -= 1
        else:
            raise Exception('invalid index passed in')

    def advance(self):
        if self.isEmpty() == False:
            curNode = self.cursor.nextNode
            self.cursor = curNode.nextNode

    def front(self):
        return self.cursor.nextNode

    def back(self):
        curNode = self.cursor.nextNode
        while curNode != self.cursor:
            if curNode.nextNode == self.cursor:
                break
        return curNode

    def reverse(self):
        nodes = []
        curNode = self.cursor.nextNode
        while curNode != self.cursor:
            nodes.append(self.remove())
            curNode = curNode.nextNode
        for _ in range(len(nodes)):
            self.insert(nodes.pop().data)
