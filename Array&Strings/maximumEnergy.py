class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        dp = [0] * n

        for i in range(n -1 , -1, -1):
            
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
        
        return max(dp)


solution = Solution()
print(solution.maximumEnergy([5, 2, -10, -5, 1], 3))
