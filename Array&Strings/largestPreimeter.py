class Solution:
    def largestPerimeter(self, nums):
        nums.sort()

        for k in range(len(nums) -1, 1, -1):
            if nums[k] <= (nums[k-1] + nums[k-2]):
                return nums[k] + nums[k-1] + nums[k-2]
            
        return 0

solution = Solution()
print(solution.largestPerimeter([2,1,2])) # 5