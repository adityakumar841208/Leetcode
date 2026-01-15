class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars, vBars):
        def max_consecutive(bars):
            if not bars:
                return 1

            bars.sort()
            longest = 1
            curr = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                longest = max(longest, curr)

            # hole size is consecutive bars + 1
            return longest + 1

        width = max_consecutive(hBars)
        height = max_consecutive(vBars)

        return min(width, height) ** 2



solution = Solution()
print(solution.maximizeSquareHoleArea(5, 5, [0,2,4], [0,3]))  # Expected output: 4