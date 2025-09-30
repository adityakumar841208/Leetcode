class Solution:
    def minScoreTriangulation(self, values):
        dp = [[-1] * 51 for _ in range(51)]

        def solve(start, end):
            if end - start + 1 < 3:
                return 0
            
            if(dp[start][end] != -1):
                return dp[start][end]
            
            minRes = float('inf')
            for i in range(start+1, end):
                dp[start][end] = values[i] * values[start] * values[end] + solve(start, i) + solve(i, end)

                minRes = min(dp[start][end], minRes)

            return minRes
        

        res = solve(0, len(values) - 1)
        return res

solution = Solution()
print(solution.minScoreTriangulation([1,3,1,4,1,5])) # 13