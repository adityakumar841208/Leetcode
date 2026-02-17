class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # dp = [[0] *  ]
        dp = [[0] * 101 for _ in range(101)]

        def solve(i, j):
            
            if i < 0 or j < 0 or i < j:
                return 0
            
            if dp[i][j] != 0:
                return dp[i][j]
            
            if i == 0 and j == 0:
                # it's the top glass
                return poured
            
            

            # equally spread the champagne
            left_up = (solve(i-1, j-1) - 1) / 2
            right_up = (solve(i-1, j) - 1) / 2

            if left_up < 0:
                left_up = 0

            if right_up < 0:
                right_up = 0

            # it might be extra champagne

            dp[i][j] = left_up + right_up
            return dp[i][j]
            

        return min(1, solve(query_row, query_glass))
        
                


solution = Solution()
print(solution.champagneTower(1, 1, 1))