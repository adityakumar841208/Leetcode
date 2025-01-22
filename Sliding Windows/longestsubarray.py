class Solution:
    def longestSubarray(self, nums):
        k = 1
        max_len = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len 
        
solution = Solution()
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1])) 
