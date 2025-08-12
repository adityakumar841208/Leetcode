# class Solution:
#     def singleNumber(self, nums):
#         result = 0
        
#         for i in range(32):
#             count = 0
#             for num in nums:
#                 if (num >> i) & 1:
#                     count += 1
            
#             if count % 2 != 0:
#                 result |= (1 << i)
        
#         # # Handle negative numbers (two's complement for 32-bit signed int)
#         if result >= 2 ** 31:
#             result -= 2 ** 32

#         return result

    
# solution = Solution()
# print(solution.singleNumber([2,2,1]))

# Approach 2

class Solution:
    def singleNumber(self, nums):
        # will be using zor property
        
        res = nums[0]
        
        for i in range(1, len(nums)):
            res ^= nums[i]
            
        return res
        