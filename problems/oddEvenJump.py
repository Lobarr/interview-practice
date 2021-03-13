from typing import List


def oddEvenJumps(A: List[int]) -> int:
    def getGreatestIndex(startIndex: int, compareIndex: int):
        greatest = 0
        greatestIndex = -1
        for index in range(startIndex, len(A)):
            if A[index] > greatest and A[index] <= A[compareIndex]:
                greatest = A[index]
                greatestIndex = index
        return greatestIndex

    def getLeastIndex(startIndex: int, compareIndex: int):
        least = 0
        leastIndex = -1
        for index in range(startIndex, len(A)):
            if A[index] < least and A[index] >= A[compareIndex]:
                least = A[index]
                leastIndex = index
        return leastIndex

    def getNextIndex(index: int) -> int:
        if (0 <= index < len(A)):
            if index % 2 == 0:
                return getLeastIndex(index + 1, index)
            else:
                return getGreatestIndex(index + 1, index)
        return -1

    print(getNextIndex(0))
    print(getNextIndex(1))
    print(getNextIndex(2))
