from ds.sLinkedList import SLinkedList

ERR_STACK_EMPTY = Exception('Stack has not elements')


class Stack:
    def __init__(self):
        self.linkedList = SLinkedList()

    def push(self, data):
        self.linkedList.insertFront(data)

    def pop(self):
        return self.linkedList.removeFront()

    def getCount(self):
        return self.linkedList.getCount()

    def peek(self):
        return self.linkedList.head if not self.linkedList.isEmpty() else None

    def printAsc(self):
        self.linkedList.printListAsc()

    def printDes(self):
        self.linkedList.printListDes()

    def isEmpty(self):
        return self.linkedList.isEmpty()


class ArrayStack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def top(self):
        if self.isEmpty():
            raise ERR_STACK_EMPTY
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            raise ERR_STACK_EMPTY
        return self.stack.pop()
