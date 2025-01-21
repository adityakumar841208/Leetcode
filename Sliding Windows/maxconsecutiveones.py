class Solution:
    def longestOnes(self, nums, k):
        count = k
        length = 0 #window length
        
        index = 0
        while count:
            if nums[index] == 0:
                count -= 1
            length += 1
            index += 1
        zeroes = 0
        
        for i in range(index, len(nums)):
            if nums[i] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[index] == 0:
                    zeroes -= 1
                index += 1
            length = max(length, i - index + 1)
            
        return length
            
        
            
        
        
solution = Solution()
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 6