from collections import deque, defaultdict
from typing import List
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()   # FIFO queue of [source, destination, timestamp]
        self.timeMap = defaultdict(list)  # destination -> sorted list of timestamps
        self.packetSet = set() # to detect duplicates (source,destination,timestamp)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # check duplicate
        if (source, destination, timestamp) in self.packetSet:
            return False

        # remove one if full
        if len(self.queue) >= self.memoryLimit:
            old_source, old_destination, old_time = self.queue.popleft()
            self.packetSet.remove((old_source, old_destination, old_time))
            idx = bisect.bisect_left(self.timeMap[old_destination], old_time)
            if idx < len(self.timeMap[old_destination]) and self.timeMap[old_destination][idx] == old_time:
                self.timeMap[old_destination].pop(idx)

        # add new packet
        self.queue.append([source, destination, timestamp])
        self.packetSet.add((source, destination, timestamp))
        bisect.insort(self.timeMap[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.packetSet.remove((source, destination, timestamp))
        idx = bisect.bisect_left(self.timeMap[destination], timestamp)
        if idx < len(self.timeMap[destination]) and self.timeMap[destination][idx] == timestamp:
            self.timeMap[destination].pop(idx)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.timeMap[destination]
        left = bisect.bisect_left(times, startTime)
        right = bisect.bisect_right(times, endTime)
        return right - left
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)