class ArrayList:
    def __init__(self, capacity):
        DEFAULT_SIZE = 2
        self.list_ = [None] * capacity
        self.capacity = capacity if capacity > 0 else DEFAULT_SIZE
        self.count = 0

    def isFull(self):
        return self.count == self.capacity

    def calculateNewCapacity(self):
        return self.capacity * 2

    def makeListFrom(self, source: list, capacity: int):
        destination = [None] * capacity
        for (index, value) in enumerate(source):
            destination[index] = value
        return destination

    def doubleCapacity(self):
        newCapcity = self.calculateNewCapacity()
        self.list_ = self.makeListFrom(self.getList(), newCapcity)
        self.capacity = newCapcity

    def insert(self, value):
        self.isFull() and self.doubleCapacity()
        self.list_[self.count] = value
        self.count += 1

    def remove(self, value):
        self.list_.remove(value)
        self.count -= 1

    def removeAt(self, index):
        if not 0 <= index <= self.count:
            raise Exception('invalid index provided')
        self.list_ = self.list_[0:index] + self.list_[index + 1:] + [None]
        self.count -= 1

    def getCapacity(self):
        return self.capacity

    def getSize(self):
        return self.count

    def getList(self):
        return self.list_

    def isEmpty(self):
        return self.count == 0

    def contains(self, value):
        return value in self.getList()
