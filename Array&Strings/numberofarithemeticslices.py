class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        count1 = 1
        
        if len(nums) < 3:
            return 0
        
        diff = nums[1] - nums[0]
        curr_count = 0
        for i in range(len(nums) -1 ):
            
            curr_diff = nums[i+1] - nums[i]
            if curr_diff == diff:
                curr_count += 1
            else:
                curr_count = 0
                diff = curr_diff
                
            if curr_count >= 3:
                # increase the count1 
                count1 += 2
            
        return count1
    
    
solution = Solution()
print(solution.numberOfArithmeticSlices([1,2,3,4]))  # ✅ 3
