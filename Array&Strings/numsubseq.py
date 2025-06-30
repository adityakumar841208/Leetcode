class Solution:
    def numSubseq(self, nums, target):
        nums.sort()
        MOD = 10**9 + 7
        res = 0
        left, right = 0, len(nums) - 1
        
        powers = [1] * len(nums)
        for i in range(1, len(nums)):
            powers[i] = (powers[i - 1] * 2) % MOD
            
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + powers[right - left]) % MOD
                left += 1
            else:
                right -= 1
                
        return res
    
solution = Solution()
print(solution.numSubseq([3, 5, 6, 7], 9))