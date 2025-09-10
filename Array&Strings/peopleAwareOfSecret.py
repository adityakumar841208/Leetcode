class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # Day 1 one person knows
        share = 0  # running count of people who can share

        for day in range(2, n + 1):
            # people start sharing today
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # people forget today
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            dp[day] = share

        # count people who still remember on day n
        ans = sum(dp[max(1, n - forget + 1): n + 1]) % MOD
        return ans
    
solution = Solution()
print(solution.peopleAwareOfSecret(6, 2, 4)) 
