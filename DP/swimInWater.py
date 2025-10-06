import heapq
class Solution:
    def swimInWater(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = 0
        visited = [[False] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        while heap:
            h, r, c = heapq.heappop(heap)

            res = max(res, h)
            if r == m - 1 and c == n - 1:
                return res #got the target
            
            for nr, nc in directions:
                updated_row = r + nr
                updated_col = c + nc

                if 0 <= updated_row < m and 0 <= updated_col < n and not visited[updated_row][updated_col]:
                    heapq.heappush(heap, (grid[updated_row][updated_col], updated_row, updated_col))
                    visited[updated_row][updated_col] = True

solution = Solution()
print(solution.swimInWater([[0,2],[1,3]]))