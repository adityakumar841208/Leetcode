class Solution:
    def minimumSum(self, grid) -> int:
        # n, m = len(grid), len(grid[0])

        # # 2D prefix for fast "any 1s in region?" checks
        # pref = [[0]*(m+1) for _ in range(n+1)]
        # ones = 0
        # for i in range(n):
        #     for j in range(m):
        #         ones += grid[i][j]
        #         pref[i+1][j+1] = grid[i][j] + pref[i][j+1] + pref[i+1][j] - pref[i][j]

        # def ones_in(r1, c1, r2, c2):
        #     return pref[r2][c2] - pref[r1][c2] - pref[r2][c1] + pref[r1][c1]

        # def bounding_area(r1, c1, r2, c2):
        #     """Area of minimal bounding box of 1s inside [r1:r2) x [c1:c2), or None if none."""
        #     if ones_in(r1, c1, r2, c2) == 0:
        #         return None
        #     min_r, max_r, min_c, max_c = n, -1, m, -1
        #     # (For clarity; can be optimized if needed.)
        #     for i in range(r1, r2):
        #         row = grid[i]
        #         for j in range(c1, c2):
        #             if row[j] == 1:
        #                 if i < min_r: min_r = i
        #                 if i > max_r: max_r = i
        #                 if j < min_c: min_c = j
        #                 if j > max_c: max_c = j
        #     return (max_r - min_r + 1) * (max_c - min_c + 1)

        # # Edge case: if total 1s <= 3, you can always use up to three 1x1 rectangles
        # # (and, if needed, place tiny "dummy" rectangles of area 1 in zero cells).
        # if ones <= 3:
        #     return 3

        # INF = 10**18
        # best = INF

        # # 1) Three vertical strips
        # for c1 in range(1, m-1):
        #     for c2 in range(c1+1, m):
        #         a = bounding_area(0, 0, n, c1)
        #         b = bounding_area(0, c1, n, c2)
        #         c = bounding_area(0, c2, n, m)
        #         if None not in (a, b, c):
        #             best = min(best, a + b + c)

        # # 2) Three horizontal strips
        # for r1 in range(1, n-1):
        #     for r2 in range(r1+1, n):
        #         a = bounding_area(0, 0, r1, m)
        #         b = bounding_area(r1, 0, r2, m)
        #         c = bounding_area(r2, 0, n, m)
        #         if None not in (a, b, c):
        #             best = min(best, a + b + c)

        # # 3) Mixed: H-first, split bottom vertically
        # for r in range(1, n):
        #     for c in range(1, m):
        #         a = bounding_area(0, 0, r, m)      # top
        #         b = bounding_area(r, 0, n, c)      # bottom-left
        #         d = bounding_area(r, c, n, m)      # bottom-right
        #         if None not in (a, b, d):
        #             best = min(best, a + b + d)

        # # 4) Mixed: H-first, split top vertically
        # for r in range(1, n):
        #     for c in range(1, m):
        #         a = bounding_area(0, 0, r, c)      # top-left
        #         b = bounding_area(0, c, r, m)      # top-right
        #         d = bounding_area(r, 0, n, m)      # bottom
        #         if None not in (a, b, d):
        #             best = min(best, a + b + d)

        # # 5) Mixed: V-first, split right horizontally  (*** new ***)
        # for c in range(1, m):
        #     for r in range(1, n):
        #         a = bounding_area(0, 0, n, c)      # left
        #         b = bounding_area(0, c, r, m)      # top-right
        #         d = bounding_area(r, c, n, m)      # bottom-right
        #         if None not in (a, b, d):
        #             best = min(best, a + b + d)

        # # 6) Mixed: V-first, split left horizontally   (*** new ***)
        # for c in range(1, m):
        #     for r in range(1, n):
        #         a = bounding_area(0, 0, r, c)      # top-left
        #         b = bounding_area(r, 0, n, c)      # bottom-left
        #         d = bounding_area(0, c, n, m)      # right
        #         if None not in (a, b, d):
        #             best = min(best, a + b + d)

        # return -1 if best == INF else best
    
    
        # second approach
        m = len(grid)
        n = len(grid[0])
        
        def foundArea(rowStart, rowEnd, colStart, colEnd, mat):
            area = 0
            
            minRow, maxRow = m, -1
            minCol, maxCol = n, -1
            
            for i in range(rowStart, rowEnd):
                for j in range(colStart, colEnd):
                    if mat[i][j] == 1:
                        if i < minRow:
                            minRow = i
                        if i > maxRow:
                            maxRow = i
                        if j < minCol:
                            minCol = j
                        if j > maxCol:
                            maxCol = j
                            
            if maxRow == -1 and maxCol == -1:
                return 0
            
            area = (maxRow - minRow + 1) * (maxCol - minCol + 1)
            return area
            
        
        result = float('inf')
        # divide the matrix into 3 parts
        for rowSplit in range(1, m):
            for colSplit in range(1, n):
                
                topSplit = foundArea(0, rowSplit, 0, n, grid)
                bottomLeftSplit = foundArea(rowSplit, m, 0, colSplit, grid)
                bottomRightSplit = foundArea(rowSplit, m, colSplit, n, grid)
                
                result = min(result, topSplit + bottomLeftSplit + bottomRightSplit)
                
                topLeftSplit = foundArea(0, rowSplit, 0, colSplit, grid)
                topRightSplit = foundArea(0, rowSplit, colSplit, n, grid)
                bottomSplit = foundArea(rowSplit, m, 0, n, grid)
                
                result = min(result, topLeftSplit + topRightSplit + bottomSplit)
        
        # vertical splits
        for colSplit1 in range(1, n-1):
            for colSplit2 in range(colSplit1+1, n):
                
                leftSplit = foundArea(0, m, 0, colSplit1, grid)
                middleSplit = foundArea(0, m, colSplit1, colSplit2, grid)
                rightSplit = foundArea(0, m, colSplit2, n, grid)
                
                result = min(result, leftSplit + middleSplit + rightSplit)
                
        # horizontal splits
        for rowSplit1 in range(1, m-1):
            for rowSplit2 in range(rowSplit1+1, m):
                
                topSplit = foundArea(0, rowSplit1, 0, n, grid)
                middleSplit = foundArea(rowSplit1, rowSplit2, 0, n, grid)
                bottomSplit = foundArea(rowSplit2, m, 0, n, grid)
                
                result = min(result, topSplit + middleSplit + bottomSplit)
                
        return result if result != float('inf') else 0
            

solution = Solution()
print(solution.minimumSum([[1,0,1,0],[0,1,0,1]]))