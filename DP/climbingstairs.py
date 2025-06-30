class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def findClimb(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in memo:
                return memo[n]

            memo[n] = findClimb(n - 1) + findClimb(n - 2)
            return memo[n]
    
        return findClimb(n)


solution = Solution()
print(solution.climbStairs(5)) 

# total ways to climb 3 stairs - 1,2 or 2,1 or 1,1,1