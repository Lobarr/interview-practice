from typing import List


class HashMap:
    def __init__(self, numBuckets=10):
        self.numBuckets = numBuckets
        self.buckets = [list() for _ in range(numBuckets)]
        self.count = 0

    def getBucketIndex(self, key):
        _hash = hash(key)
        return _hash % self.numBuckets

    def get(self, key):
        bucketIndex = self.getBucketIndex(key)
        for entry in self.buckets[bucketIndex]:
            if entry['key'] == key:
                return entry['value']
        raise KeyError(f'Unable to find key {repr(key)}')

    def set_(self, key, value):
        bucketIndex = self.getBucketIndex(key)
        self.buckets[bucketIndex].append({"key": key, "value": value})
        self.count += 1

    def remove(self, key):
        bucketIndex = self.getBucketIndex(key)
        bucket = self.buckets[bucketIndex]
        for entry in self.buckets[bucketIndex]:
            if entry['key'] == key:
                bucket.remove(entry)
                self.count -= 1


class SortedMap:
    class Item:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

        def getKey(self):
            return self.key

        def setValue(self, value):
            self.value = value

    def __init__(self):
        self.table: List[SortedMap.Item] = []

    def getCount(self):
        return len(self.table)

    def findIndex(self, key, lowIndex, highIndex):
        if lowIndex > highIndex:
            return highIndex + 1  # position where key is supposed to be
        else:
            mid = (lowIndex + highIndex) // 2
            if key == self.table[mid].getKey():
                return mid
            elif key < self.table[mid].getKey():
                return self.findIndex(key, lowIndex, mid - 1)
            else:
                return self.findIndex(key, mid + 1, highIndex)

    def getKey(self, key):
        keyIndex = self.findIndex(key, 0, self.getCount() - 1)
        if (keyIndex is self.getCount()
                or self.table[keyIndex].getKey() != key):
            raise KeyError()
        return self.table[keyIndex]

    def setKey(self, key, value):
        keyIndex = self.findIndex(key, 0, self.getCount() - 1)
        if (keyIndex < self.getCount()
                and self.table[keyIndex].getKey() == key):
            self.table[keyIndex].setValue(value)
        else:
            newItem = SortedMap.Item(key, value)
            self.table.insert(keyIndex, newItem)

    def removeKey(self, key):
        keyIndex = self.findIndex(key, 0, self.getCount() - 1)
        if (keyIndex is self.getCount()
                or self.table[keyIndex].getKey() != key):
            raise KeyError()
        self.table.pop(keyIndex)

    def findMin(self):
        if self.getCount() > 0:
            return self.table[0]
        return None

    def findMax(self):
        if self.getCount() > 0:
            return self.table[-1]
        return None

    def findGreaterOrEqaual(self, key):
        keyIndex = self.findIndex(key, 0, self.getCount() - 1)
        if keyIndex < self.getCount():
            return self.table[keyIndex]
        return None

    def findGreaterThan(self, key):
        keyIndex = self.findIndex(key, 0, self.getCount() - 1)
        if (keyIndex < self.getCount()
                and self.table[keyIndex].getKey() == key):
            keyIndex += 1

        if keyIndex < self.getCount():
            return self.table[keyIndex]
        return None

    def findLessthan(self, key):
        keyIndex = self.findIndex(key, 0, self.getCount() - 1)
        if keyIndex > 0:
            return self.table[keyIndex - 1]
        return None

    def findRange(self, start, stop):
        items = []
        keyIndex = self.findIndex(start, 0, self.getCount() - 1)
        while (keyIndex < self.getCount()
               and (stop is None or self.table[keyIndex].getKey() < stop)):
            items.append(self.table[keyIndex])
            keyIndex += 1
        return items
