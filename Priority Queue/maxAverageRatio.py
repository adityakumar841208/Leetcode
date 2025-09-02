# ...existing code...
import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t

        return total / len(classes)

# ...existing code...
solution = Solution()
print(solution.maxAverageRatio([[1,2],[3,5],[2,2]], 2))