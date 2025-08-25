class Solution:
    def longestSubarray(self, nums) -> int:
        # max_sum = 0
        # zero_count = 0
        # i = 0
        
        # for j in range(len(nums)):
            
        #     if nums[j] == 0:
        #         zero_count += 1

        #     while zero_count > 1:
        #         if nums[i] == 0:
        #             zero_count -= 1
        #         i += 1
                
        #     max_sum = max(max_sum, j - i)
        
        # return max_sum if len(nums) != max_sum else max_sum - 1
        # max_sum = 0
        # zero_count = 0
        # curr_sum = 0
        # zero_index = -1

        # for j in range(len(nums)):
        #     if nums[j] == 1:
        #         curr_sum += 1
        #     else:
        #         zero_count += 1
        #         if zero_count == 1:
        #             zero_index = j
        #         elif zero_count == 2:
        #             curr_sum = j - zero_index - 1
        #             zero_index = j
        #             zero_count = 1   # keep only the latest zero

        #     max_sum = max(curr_sum, max_sum)
                    
        # return max_sum if max_sum < len(nums) else max_sum - 1
        max_sum = 0
        last_zero = -1    # last seen zero
        prev_zero = -1    # second last seen zero
        i = 0
        
        while i < len(nums):
            if nums[i] == 0:
                prev_zero = last_zero
                last_zero = i
            max_sum = max(max_sum, i - prev_zero - 1)
            i += 1

        return max_sum
    
solution = Solution()
print(solution.longestSubarray([1,1,0,1]))