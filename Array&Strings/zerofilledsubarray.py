class Solution:
    def zeroFilledSubarray(self, nums):
        
        # approach 1
        # curr_sum = 0
        # i = 0
        # nums_len = len(nums)
        
        # while i < nums_len:
            
        #     if nums[i] == 0:
        #         count = 0
        #         while nums[i] == 0:
        #             count += 1
        #             i += 1       
        #         curr_sum += count * (count + 1) // 2
              
        #     i+= 1
            
        # return curr_sum
        
        # approach 2
        # observation - currlen of subarray is the len of prev =  index + currLen
        curr_sum = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            curr_sum += count
                
        return curr_sum
    
    
solution = Solution()
print(solution.zeroFilledSubarray([1,3,0,0,2,0,0,4]))  # ✅ 8