class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        res = 0

        # compare every pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # intersection rectangle
                left   = max(bottomLeft[i][0], bottomLeft[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                right  = min(topRight[i][0], topRight[j][0])
                top    = min(topRight[i][1], topRight[j][1])

                width = right - left
                height = top - bottom

                if width > 0 and height > 0:
                    side = min(width, height)
                    res = max(res, side * side)

        return res


solution = Solution()
print(solution.largestSquareArea([[2,2],[2,3]], [[4,3],[3,4]]))
