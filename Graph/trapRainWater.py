import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # (height, row, col)

        # Push all boundary cells into heap
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        res = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Process cells
        while heap:
            height, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # visited[nr][nc] = True
                    # # If neighbor is lower, trap water
                    # if heightMap[nr][nc] < height:
                    #     res += height - heightMap[nr][nc]
                    #     heapq.heappush(heap, (height, nr, nc))
                    # else:
                    #     heapq.heappush(heap, (heightMap[nr][nc], nr, nc))
                    res += max(height, - heightMap[nr][nc], 0) # if the neighbour is lower add 0
                    heapq.heappush(heap, (max(height, - heightMap[nr][nc]),nr, nc))
                    visited[nr][nc] = True

        return res


# Test
solution = Solution()
print(solution.trapRainWater(
    [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1],
    ]
))  # ✅ Expected output = 4
