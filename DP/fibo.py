class Solution:
    def fibo(self, n: int) -> int:
        
        # bottom up approach
        if n == 0 or n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        print(dp)
        return dp[n]
    
    # top down approach
    # def fibo(self, n: int) -> int:
    #     memo = {}
#         def findFibo(n):
#             if n in memo:
#                 return memo[n]
    #         if n == 0 or n == 1:
    #               return 1
    #         memo[n] = findFibo[n-1] + findFibo[n-2
    #         return memo
            

solution = Solution()
print(solution.fibo(5), end=' ')  # Output: 5