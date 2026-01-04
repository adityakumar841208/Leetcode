class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        initialColorState = []
        colors = ['R', 'G', 'B']

        # generate all valid column states
        def generateColumnStates(currentState, prev):
            if len(currentState) == m:
                initialColorState.append(currentState)
                return

            for color in colors:
                if color != prev:
                    generateColumnStates(currentState + color, color)

        generateColumnStates("", "")

        # 🔹 explicit memo table
        dp = {}

        def solve(remainingCol, prevIdx):
            if remainingCol == 0:
                return 1

            # 🔹 memo check
            if (remainingCol, prevIdx) in dp:
                return dp[(remainingCol, prevIdx)]

            prevState = initialColorState[prevIdx]
            ways = 0

            for j_idx, j in enumerate(initialColorState):
                canPlace = True
                for k in range(m):
                    if prevState[k] == j[k]:
                        canPlace = False
                        break

                if canPlace:
                    ways = (ways + solve(remainingCol - 1, j_idx)) % MOD

            # 🔹 memo store
            dp[(remainingCol, prevIdx)] = ways
            return ways

        result = 0
        for i in range(len(initialColorState)):
            result = (result + solve(n - 1, i)) % MOD

        return result




solution = Solution()

print(solution.colorTheGrid(1, 1))  # Expected output: 3