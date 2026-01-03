class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # same: patterns like ABA (2 colors)
        # diff: patterns like ABC (3 colors)
        same = 6   # ABA patterns for first row
        diff = 6   # ABC patterns for first row

        for _ in range(1, n):
            new_same = (same * 3 + diff * 2) % MOD
            new_diff = (same * 2 + diff * 2) % MOD
            same, diff = new_same, new_diff

        return (same + diff) % MOD


solution = Solution()
print(solution.numOfWays(1))  # 12
print(solution.numOfWays(2))  # 54
