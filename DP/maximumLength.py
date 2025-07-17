class Solution:
    def maximumLength(self, nums) -> int:
        #  approach = Dynamic Problem
        # 1. go to top down using for loop
        
        countOdd = 0
        countEven = 0
        countAlternate = 1
        
        if len(nums) == 0:
            return 0
        
        for num in nums:
            if num % 2 == 0:
                countEven += 1
            else:
                countOdd += 1
        
        parity = nums[0] % 2
        
        for i in range(1,len(nums)):
            currParity = nums[i] % 2
            if currParity != parity:
                countAlternate += 1
                parity = currParity

        return max(countOdd, countEven, countAlternate)
    
solution = Solution()
print(solution.maximumLength([1, 3]))  # Example usage

# 4