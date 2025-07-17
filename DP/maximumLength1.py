class Solution:
    def maximumLength(self, nums, k):
        
        dp = dp = [[0]*len(nums) for _ in range(k)]
        
        maxSub = 1
        
        for i in range(1,len(nums)):
            for j in range(i):
                
                mod = (nums[j] + nums[i]) % k 
                dp[mod][i] = max(dp[mod][i], 1+ dp[mod][j])
                maxSub = max(maxSub, dp[mod][i])
                
        return maxSub
    
solution = Solution()
print(solution.maximumLength([1, 2, 3, 4, 5],2))