class Solution:
    def distributeCandies(self, n, limit):
        total = 0
        
        def findIteration(curr,tar, iteration):
            sum = 0
            if iteration > 3:
                return 0
            
            for i in range(limit+1):
                if iteration == 3 and tar - i == 0:
                        return sum + 1
                        
                if tar-i >= 0 and i <= limit: 
                    sum += findIteration(curr+[i],tar-i,iteration+1)
                    
            return sum
        
        for i in range(limit+1):
            total += findIteration([i],n-i,2)
             
        return total
    
        
solution = Solution()
print(solution.distributeCandies(3,3))

# optimal one - 
# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         if n == 0 or limit == 0:
#             return 0
#         if n > limit * 3:
#             return 0
        
#         dp = [0] * (n + 1)
#         dp[0] = 1
        
#         for i in range(1, limit + 1):
#             for j in range(n, i - 1, -1):
#                 dp[j] += dp[j - i]
        
#         return dp[n]