class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cost.append(0)  # Add zero cost for top
        
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = cost[0]
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]

    
    
solution = Solution()
print(solution.minCostClimbingStairs([10, 15, 20]))  # Output: 15