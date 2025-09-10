class Solution:
    def minSubArrayLen(self, target: int, nums):
        
        res = len(nums)
        start = 0 #index of start
        arr_sum = 0 #sum
        i = 0
        
        while i < len(nums):
            
            arr_sum += nums[i]
            while target < arr_sum:
                arr_sum -= nums[start]
                start += 1
                
            if arr_sum == target:
                print('here i am', arr_sum)
                res = min(res, i - start + 1)
            
            i += 1
            
        return 0 if res == len(nums) else res
        
solution = Solution()
print(solution.minSubArrayLen(11, [1,2,3,4,5]))
    