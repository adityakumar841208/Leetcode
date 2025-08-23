class Solution:
    def countSquares(self, matrix):
        # squareCount = 0
        # m = len(matrix)
        # n = len(matrix[0])
        
        # memo = [[0] * n for _ in range(m)]
        
        # def exploreSquares(matrix_copy, row, col, memo):
        #     # base case
        #     if row < m and col < n:
        #         if matrix_copy[row][col] == 0:
        #             return 0
                
        #         if memo[row][col] != 0:
        #             return memo[row][col]
                
        #         bottom = exploreSquares(matrix_copy, row + 1, col, memo)
        #         right = exploreSquares(matrix_copy, row, col + 1, memo)
        #         diagonal = exploreSquares(matrix_copy, row + 1, col + 1, memo)
                   
                   
        #         memo[row][col] = 1 + min(bottom, right, diagonal)
        #         return memo[row][col]
            
        #     return 0
        
        # for i in range(m):
        #     for j in range(n):
                
        #         if matrix[i][j] == 1:
        #             squareCount += exploreSquares(matrix, i, j, memo)
        
        # return squareCount
        
        # bottom up approach
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        count = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # go upside left, up and diagonal
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]
        return count
    
solution = Solution()
print(solution.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))