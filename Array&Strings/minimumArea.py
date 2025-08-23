class Solution:
    def minimumArea(self, grid):
        
        maxRow = 0
        minRow = len(grid)
        maxCol = 0
        minCol = len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    maxRow = max(maxRow, i)
                    minRow = min(minRow, i)
                    maxCol = max(maxCol, j)
                    minCol = min(minCol, j)
                    
        return (maxRow - minRow + 1) * (maxCol - minCol + 1) if maxRow >= minRow and maxCol >= minCol else 0
                
    
solution = Solution()
print(solution.minimumArea( [[1,0],[0,0]])) # expected 4