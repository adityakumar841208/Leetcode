class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        res = []
        row, col = 0, 0
        direction = 1  # 1 = up, -1 = down

        for _ in range(m * n):
            res.append(mat[row][col])

            if direction == 1:  # moving up
                if col == n - 1:      # hit right boundary
                    row += 1
                    direction = -1
                elif row == 0:        # hit top boundary
                    col += 1
                    direction = -1
                else:                 # normal move
                    row -= 1
                    col += 1
            else:  # moving down
                if row == m - 1:      # hit bottom boundary
                    col += 1
                    direction = 1
                elif col == 0:        # hit left boundary
                    row += 1
                    direction = 1
                else:                 # normal move
                    row += 1
                    col -= 1

        return res

    
solution = Solution()
print(solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))