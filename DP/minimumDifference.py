import heapq

class Solution:
    def minimumDifference(self, nums):
        
        n = len(nums) // 3
        left = [0] * (2 * n + 1)
        right = [0] * (2 * n + 1)
        
        max_heap = []
        left_sum = sum(nums[:n])
        for x in nums[:n]:
            heapq.heappush(max_heap, -x)
        left[n] = left_sum
        
        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i]
            left_sum += heapq.heappop(max_heap)  # subtract largest (remember it's negative)
            left[i + 1] = left_sum
        
            # Now do the right part (maximize n elements from last 2n..3n)
            min_heap = []
            right_sum = sum(nums[-n:])
            for x in nums[-n:]:
                heapq.heappush(min_heap, x)
            right[2 * n] = right_sum
            
            for i in range(2 * n - 1, n - 1, -1):
                heapq.heappush(min_heap, nums[i])
                right_sum += nums[i]
                right_sum -= heapq.heappop(min_heap)
                right[i] = right_sum
            
            ans = float('inf')
            for i in range(n, 2 * n + 1):
                ans = min(ans, left[i] - right[i])
            
            return ans
        
solution = Solution()
print(solution.minimumDifference([1, 2, 3, 4, 5, 6]))  # Example usage