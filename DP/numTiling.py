class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] * 2) % (10**9 + 7)

        return dp[n]
    
    
solution = Solution()
print(solution.numTilings(3))  # Output: 5