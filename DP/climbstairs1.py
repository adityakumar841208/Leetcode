class Solution:
    def climbStairs(self, n: int) -> int:
        # i'll be using top down approach
        
        memo = {}
        
        def climb(n,dp):
            if n <= 2:
                return n
            
            if n in dp:
                return dp[n]
            
            dp[n] = climb(n-1,dp) + climb(n-2,dp)
                
        
            return dp[n]
        
        return climb(n,memo)
     
solution = Solution()
print(solution.climbStairs(5)) # Output: 8, as there are 8 distinct ways to climb 5 stairs