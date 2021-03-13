from heapq import heapify, heappop, heappush


class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end

    def __lt__(self, other):
        return self.getEnd() < other.getEnd()


def sortByStart(interval: Interval):
    return interval.getStart()


def meetingRoomII(meetings: list):
    if not meetings:
        return 0

    intervals = [Interval(meeting[0], meeting[1]) for meeting in meetings]
    earliests = []

    intervals.sort(key=sortByStart)
    heappush(earliests, intervals[0])

    for i in range(1, len(intervals)):
        cur = intervals[i]
        earliest = heappop(earliests)

        if (cur.getStart() >= earliest.getEnd()):
            earliest.setEnd(cur.getEnd())
        else:
            heappush(earliests, cur)

        heappush(earliests, earliest)

    return len(earliests)
