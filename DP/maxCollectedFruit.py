class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)

        # Step 1: Child 1 collects fruits along the diagonal
        fruits_count = 0
        for i in range(n):
            fruits_count += fruits[i][i]

        # Step 2: Child 2 dynamic collection using DP
        dp = [[0] * n for _ in range(n)]

        # Start from bottom-left corner
        dp[n - 1][0] = fruits[n - 1][0]

        def find_fruit(child_name, i, j, dp, fruits):
            max_count = 0

            if child_name == 'child2':
                ways = [[i - 1, j], [i - 1, j + 1]]  # up, up-right
            else:
                ways = [[i + 1, j - 1], [i + 1, j]]  # for child1 if needed in future

            for new_i, new_j in ways:
                if 0 <= new_i < n and 0 <= new_j < n:
                    if dp[new_i][new_j] == 0:
                        dp[new_i][new_j] = dp[i][j] + fruits[new_i][new_j]
                    else:
                        dp[new_i][new_j] = max(dp[new_i][new_j], dp[i][j] + fruits[new_i][new_j])

                    max_count = max(max_count, dp[new_i][new_j])

            return max_count

        # Fill the dp table for child2 by simulating all possible moves
        for i in range(n - 1, -1, -1):      # from bottom to top
            for j in range(n):              # from left to right
                if dp[i][j] > 0:
                    find_fruit('child2', i, j, dp, fruits)


        child2_fruits = max(max(row) for row in dp)


        return fruits_count + child2_fruits  

    
solution = Solution()
print(solution.maxCollectedFruits([[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]))  # Example usage