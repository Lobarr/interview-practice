# from problems.meetingRoom2 import meetingRoomII
from ds.sLinkedList import *

if __name__ == '__main__':
    s = SLinkedList()
    s.insertFront(1)
    s.insertFront(2)
    s.printListAsc()
    print()

    print(s.getNodeAtIndex(0).data)
    print(s.getNodeAtIndex(1).data)
    print(s.search(1))
    print(s.search(-1))
    print()
    s.printListDes()
    print()

    print(f'prev count {s.count}')
    s.insertAt(s.count, 3)
    s.insertAt(0, 100)
    s.printListAsc()
    print(f'new count {s.count}')
    s.removeAt(s.count - 1)
    s.printListAsc()

