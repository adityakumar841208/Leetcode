class Solution:
    def minimumTotal(self, triangle):

        # t = triangle

        # for row in range(len(triangle)-2, -1, -1):
            
        #     for col in range(row+1):

        #         t[row][col] = t[row][col] + min(t[row+1][col], t[row+1][col+1])

        # return t[0][0]

        t = triangle[-1]

        for row in range(len(triangle)-2, -1, -1):
            
            for col in range(row+1):

                t[col] = triangle[row][col] + min(t[col], t[col+1])

        
        return t[0]


solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # 11