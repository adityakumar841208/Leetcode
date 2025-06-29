import heapq

class Solution:
    def maxSubsequence(self, nums, k):

        # Store each element with its index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Get the k largest elements based on value
        k_largest = heapq.nlargest(k, indexed_nums, key=lambda x: x[0])
        
        # Sort the selected elements based on their original index to maintain order
        k_largest.sort(key=lambda x: x[1])
        
        # Extract just the numbers (not indices)
        result = [num for num, _ in k_largest]
        
        return result
    
solution = Solution()
print(solution.maxSubsequence([3, 4, 3, 2], 2))
