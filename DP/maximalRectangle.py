class Solution:
    def maximalRectangle(self, matrix):
        max_area = 0
        pefix_matrix = []

        # make prefix sum
        for i in range(len(matrix)):
            pefix_matrix.append([0] * len(matrix[0]))
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    pefix_matrix[i][j] = pefix_matrix[i][j - 1] + 1 if j > 0 else 1

        # count rectangle
        for i in range(len(pefix_matrix)):
            for j in range(len(pefix_matrix[0])):
                if pefix_matrix[i][j] == 0:
                    continue
                width = pefix_matrix[i][j]
                for k in range(i, -1, -1):
                    width = min(width, pefix_matrix[k][j])
                    if width == 0:
                        break
                    height = i - k + 1
                    max_area = max(max_area, width * height)

        return max_area

solution = Solution()
print(solution.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))