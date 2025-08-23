class Solution:
    def numSubmat(self, mat) -> int:
        
        row = len(mat) # row
        col = len(mat[0]) #col
        subArrayCount = 0
        
        # def exploreSubArray(matrix, row, col):
            
        #     # base case
        #     if row >= m or col >= n:
        #         return 0
            
        #     if matrix[row][col] != 1:
        #         return 0
            
        #     left = exploreSubArray(matrix, row+1, col)
        #     right = exploreSubArray(matrix, row, col+1)
        #     diagonal = exploreSubArray(matrix, row+1 , col+1)
            
            
        #     return 1 + min(left, right, diagonal)
        
        
        # def exploreLine(mat_copy, row, col, curr, first=True):
        #     if row >= m or col >= n:
        #         return 0
        #     if mat_copy[row][col] == 0:
        #         return 0
            
        #     if curr == "row":
        #         return (0 if first else 1) + exploreLine(mat_copy, row, col+1, "row", False)
        #     if curr == "col":
        #         return (0 if first else 1) + exploreLine(mat_copy, row+1, col, "col", False)
        #     return 0


        # for i in range(m):
        #     for j in range(n):
                
        #         if mat[i][j] == 1:
        #             subArrayCount += exploreLine(mat, i, j, "row")
        #             subArrayCount += exploreLine(mat, i, j, "col")
        #             subArrayCount += exploreSubArray(mat, i, j)
        
        # return subArrayCount
        # optimal one
        
        dp = [[0]*col for _ in range(row)]
        ways = [[-1, 0], [0, -1], [-1, -1]]
        
        for i in range(row):
            for j in range(col):
                
                if mat[i][j] == 1:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        for way_zero, way_one in ways:
                            dup_row = i + way_zero
                            dup_col = j + way_one
                            
                            # if dup_row < m and dup_col < n and dup >= 0:
                            if 0 <= dup_row < row and 0 <= dup_col < col:
                                if dp[dup_row][dup_col]:
                                    dp[i][j] += 1 + dp[dup_row][dup_col]
                         
                subArrayCount += dp[i][j]
                
        return subArrayCount
    
    
solution = Solution()
print(solution.numSubmat([[1,0,1],[1,1,0],[1,1,0]]))
    
    