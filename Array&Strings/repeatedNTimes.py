class Solution:
    def repeatedNTimes(self, nums):
        
        seen = {}

        for num in nums:
            
            seen[num] = seen.get(num, 0) + 1

            if seen[num] > 1:
                return num

solution = Solution()

print(solution.repeatedNTimes([1,2,3,3]))  # Output: 3
