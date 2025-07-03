class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        count = 0
        
        n = len(word)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        dp[0][0] = 1  # Base case: one way to form an empty string with 0 characters
        
        for i in range(1, n + 1):
            for j in range(k + 1):
                # If we don't take the current character
                dp[i][j] = dp[i - 1][j]
                
                # If we take the current character
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
                    
        # The answer is the number of ways to form a string of length n with exactly k characters
        for j in range(k + 1):
            count += dp[n][j]
            
        # Return the total count of possible strings        
        
        return count
    
solution = Solution()
print(solution.possibleStringCount("aabbccdd",7))