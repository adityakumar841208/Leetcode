import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        total_cost = 0
        n = len(costs)
        
        left_heap = []
        right_heap = []
        
        # Initial fill of heaps
        l, r = 0, n - 1
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, costs[l])
                l += 1
            if l <= r:
                heapq.heappush(right_heap, costs[r])
                r -= 1
        
        for _ in range(k):
            # Choose from the smaller top between both heaps
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total_cost += heapq.heappop(left_heap)
                if l <= r:
                    heapq.heappush(left_heap, costs[l])
                    l += 1
            else:
                total_cost += heapq.heappop(right_heap)
                if l <= r:
                    heapq.heappush(right_heap, costs[r])
                    r -= 1
        
    #     return total_cost
    def totalCost(self, costs, k, candidates):
        # approach take two heaps
        # you are done
        total_cost = 0
        n = len(costs)
        
        l, r = 0, n-1
        
        left_heap = []
        right_heap = []
        
        # start filling the heaps
        for i in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, costs[l])
                l += 1
                
            if l <= r:
                heapq.heappush(right_heap, costs[r])
                r -= 1
                
        for _ in range(k):
            
            if right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                # push the current data and remove from the list
                total_cost += heapq.heappop(left_heap)
                if l <= r:
                    heapq.heappush(left_heap, costs[l])
                    l += 1
            else:
                total_cost += heapq.heappop(right_heap)
                if l <= r:
                    heapq.heappush(right_heap, costs[r])
                    r -= 1
        
        return total_cost


solution = Solution()
print(solution.totalCost([1, 2, 4, 1], 3, 3))  # Output: 4
