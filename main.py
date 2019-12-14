from queue import Queue
from problems.fruitIntoBasket import totalFruit
from problems.oddEvenJump import oddEvenJumps
from problems.licenceKeyFormatting import licenseKeyFormatting
from problems.wateringCans import wateringCans
from problems.soloDomino import soloDomino
from problems.stringCompression import testStringCompression

# from typing import List
# from ds.hashTable import HashTable
# from ds.arrayList import ArrayList
# from ds.dLinkedList import DLinkedList
# from ds.stringBuilder import StringBuilder
# from ds.stack import Stack
# from ds.queue import Deque, ArrayQueue, DLLQueue
# from problems.isUnique import isUnique
# from problems.checmPermuation import checkPermutation
from problems.urlify import urlify

testStringCompression()

# print(sorted([3,2,1], ))

# queue = Queue()
# for i in range(5):
#   queue.enqueue(i)
#   queue.printAsc()
#   print('\n')
# queue.dequeue()
# queue.printAsc()

# stack = Stack()
# for i in range(5):
#   stack.push(i)
#   stack.printAsc()
#   print("\n")
# stack.pop()
# stack.printAsc()

# ll = CLinkedList()

# print(insertionSortAsc([4,3,23,3,6,7,4,4,42,345,52,3,3452][::-1]))

# print(spiralMatrix(matrix_1x3))

# dLinkedList = DLinkedList()
# for i in range(5):
#   dLinkedList.insertFront(i)
# dLinkedList.printListAsc()
# dLinkedList.removeAt(0)
# print('\n')
# dLinkedList.printListAsc()
 

# print(spiralMatrix(matrix_3x3))
# print('\n')
# print(spiralMatrix(matrix_4x4))
# print('\n')
# print(spiralMatrix(matrix_5x5))


# hashTable = HashTable()
# hashTable.set_("this", "that")
# hashTable.set_("that", "this")
# print(hashTable.get("this"))
# print(hashTable.get("that"))
# hashTable.remove("this")
# print(hashTable.get("this"))


# arrayList = ArrayList(2)
# for i in range(20):
#   arrayList.insert(i)
# print(arrayList.getList())
# arrayList.removeAt(0)
# print(arrayList.getList())

# stringBuilder = StringBuilder()
# for i in range(10):
#   stringBuilder.append(f"work{i}")
# print(stringBuilder.toString())

# print(isUnique("abcd"))

# print(checkPermutation("abc", "bac"))

# print(urlify("Mr John Smith     ", 13))

# print(palindromePermutation("Tact Coa"))

# print(oneAway("pale", "ple"))
# print(oneAway("pales", "pale"))
# print(oneAway("pale", "bale"))
# print(oneAway("pale", "bake"))

# arrQueue = ArrayQueue(5)
# arrQueue.enqueue(5)
# arrQueue.enqueue(4)
# arrQueue.enqueue(3)
# arrQueue.enqueue(2)
# arrQueue.enqueue(1)
# arrQueue.enqueue(0)
# arrQueue.printQueue()
# arrQueue.dequeue()
# arrQueue.printQueue()
# print(len(arrQueue.queue))


# deque = Deque(5)
# deque.insertLast(5)
# deque.insertFirst(4)
# deque.insertLast(6)
# deque.printQueue()
# deque.removeFirst()
# deque.removeLast()
# deque.printQueue()


# def plusOne(digits: List[int]) -> List[int]:
#   newDigits = [None] * len(digits)
#   digits[-1] = digits[-1] + 1
#   carry = False
#   for index in range(len(digits)-1, -1, -1):
#     digit = (digits[index] + 1) if carry else digits[index]
#     print(index, carry)
#     carry = False
#     if digit > 9:
#       newDigits[index] = 0
#       carry = True
#       if index == 0:
#         newDigits.insert(0, 1)
#     else:
#       newDigits[index] = digit
#   return newDigits

# print(plusOne([9,9,9,9]))

# print(oddEvenJumps([10,13,12,14,15]))
# print(licenseKeyFormatting('2-5g-3-J', 2))
# print(licenseKeyFormatting('2-4A0r7-4k', 4))

# print(totalFruit([0,1,2,2]))
# print(totalFruit([1,2,3,2,2]))
# print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
# print(totalFruit([1,0,2,3,4]))
# print(totalFruit(list(reversed([0,1,6,6,4,4,6]))))


# print(wateringCans([2, 3, 4, 3, 5, 1, 2], 6))

# print(soloDomino([1,2,3,6,4,3], [2,1,2,2,2,4], 2))

# test = {}
# print('prior ', test.keys())
# exec('global test; test[1]=1; print(globals());', {'test': test})
# print('post ', test.keys())
# # print(test.get())
