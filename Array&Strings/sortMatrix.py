class Solution:
    def sortMatrix(self, grid):
        n = len(grid)

        # diagonals starting from first row (top-right triangle) → ascending
        for col in range(1, n):  # exclude main diagonal col=0
            arr = []
            i, j = 0, col
            while i < n and j < n:
                arr.append(grid[i][j])
                i += 1
                j += 1

            arr.sort()   # ascending for top-right

            i, j, idx = 0, col, 0
            while i < n and j < n:
                grid[i][j] = arr[idx]
                i += 1
                j += 1
                idx += 1

        # diagonals starting from first column (bottom-left + main diagonal) → descending
        for row in range(n):  # include row=0 for main diagonal
            arr = []
            i, j = row, 0
            while i < n and j < n:
                arr.append(grid[i][j])
                i += 1
                j += 1

            arr.sort(reverse=True)   # descending for bottom-left

            i, j, idx = row, 0, 0
            while i < n and j < n:
                grid[i][j] = arr[idx]
                i += 1
                j += 1
                idx += 1

        return grid

solution = Solution()
print(solution.sortMatrix([[1]]))