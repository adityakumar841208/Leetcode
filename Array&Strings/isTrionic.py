class Solution:
    def isTrionic(self, nums):
        
        trend = 1
        flag = False
        n = len(nums)

        if nums[0] >= nums[1]:
            return False

        for i in range(n):

            if (i + 1) < n and nums[i] == nums[i+1]:
                return False

            if trend == 1:
                if (i + 1) < n:
                    if nums[i] > nums[i+1]:
                        trend = 2
                    continue
                else:
                    return flag

            if trend == 2:
                if (i + 1) < n:
                    if nums[i] < nums[i+1]:
                        trend = 3
                    continue
                else:
                    return flag

            if trend == 3:
                if (i + 1) < n and nums[i] > nums[i+1]:
                    flag = False
                    break
                else:
                    flag = True

        return flag        


# approach 2 clean solution
# class Solution:
#     def isTrionic(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n < 4:
#             return False

#         trend = 1   # 1 = inc, 2 = dec, 3 = inc again

#         for i in range(n - 1):

#             if nums[i] == nums[i + 1]:
#                 return False

#             if trend == 1:
#                 if nums[i] > nums[i + 1]:
#                     trend = 2

#             elif trend == 2:
#                 if nums[i] < nums[i + 1]:
#                     trend = 3

#             else:  # trend == 3
#                 if nums[i] > nums[i + 1]:
#                     return False

#         return trend == 3

   

solution = Solution()
print(solution.isTrionic([1,6,6,3,7]))