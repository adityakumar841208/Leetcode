class Solution:
    def countHillValley(self, nums):
        hill = 0
        valley = 0
        
        for i in range(1,len(nums)-1):

            left = i-1
            right = i+1
            
            if nums[left] < nums[i] > nums[right]:
                hill += 1
                continue
                
            if nums[left] == nums[i]:
                while left > 0 and nums[left] == nums[i]:
                    left -= 1
                    
            if nums[right] == nums[i]:
                while right > len(nums) and nums[right] == nums[i]:
                    right += 1
                    
            if nums[left] > nums[i] and nums[right] > nums[i]:
                valley += 1
                
        return hill + valley
    
solution = Solution()
print(solution.countHillValley([6,6,5,5,4,1]))

                

                

                
            

            
            

                    