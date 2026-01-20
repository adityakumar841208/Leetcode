class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = (10**9) + 7
        hFences.add(1)
        hFences.add(m)
        vFences.add(1)
        vFences.add(n)

        sorted(hFences)
        sorted(vFences)

        heights = set()
        widths = set()

        for bar, index in enumerate(hFences):
            for bar2, index2 in enumerate(hFences):

                if index != index2:
                    heights.add(bar2-bar)

        for bar, index in enumerate(vFences):
            for bar2, index2 in enumerate(vFences):

                if index != index2:
                    widths.add(bar2-bar)

        return (min(heights, widths) ** 2) % MOD
        

solution = Solution()
print(solution.maximizeSquareArea(5, 4, [1, 2, 4], [1, 3]))  # Output: 4