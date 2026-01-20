class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        maxSide = min(m, n)

        # Any 1x1 square is magic
        if maxSide == 1:
            return 1

        def isMagic(r, c, size):
            target = sum(grid[r][c:c+size])

            # rows
            for i in range(r, r + size):
                if sum(grid[i][c:c+size]) != target:
                    return False

            # columns
            for j in range(c, c + size):
                if sum(grid[i][j] for i in range(r, r + size)) != target:
                    return False

            # diagonals
            if sum(grid[r+i][c+i] for i in range(size)) != target:
                return False

            if sum(grid[r+i][c+size-1-i] for i in range(size)) != target:
                return False

            return True

        # Try larger squares first
        for size in range(maxSide, 1, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if isMagic(i, j, size):
                        return size

        return 1

solution = Solution()
print(solution.largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))