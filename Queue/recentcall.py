from collections import deque

class RecentCounter:
    def __init__(self):
        # Queue to store timestamps
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add the new request time to the queue
        self.queue.append(t)
        # Remove requests that are outside the [t - 3000, t] range
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        # Return the number of requests in the range
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Time complexity: O(Q), where Q is the number of queries made to the ping function.
# Space complexity: O(W), where W = 3000 is the size of the window we are considering.


counter =  RecentCounter()
print(counter.ping(1))

