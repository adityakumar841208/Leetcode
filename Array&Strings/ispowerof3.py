class Solution:
    def isPowerOfThree(self, n):
        
        return n > 0 and 1162261467 % n == 0
        
        
solution = Solution()
print(solution.isPowerOfThree(-1))