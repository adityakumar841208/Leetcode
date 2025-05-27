class Solution:
    def findPeakElement(self, nums):
        left , right = 0, len(nums) - 1
        sorted_nums = sorted(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
                
        result = nums.index(nums[left])
        if result == -1:
            return left + 1
        else:
            return result
    
solution = Solution()
print(solution.findPeakElement([1,2,1,3,5,6,4])) # 2