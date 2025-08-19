class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        # Check if n is a power of 2 and if it has an even number of trailing zeros
        return (n & (n - 1)) == 0 and (n - 1) % 3 == 0
    
solution = Solution()
print(solution.isPowerOfFour(128))  # True