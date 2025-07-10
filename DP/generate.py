class Solution:
    def generate(self, numRows):
        
        # will start from top down approach
        triangle = []
        
        for i in range(numRows):
            # create a new row
            row = [1] * (i + 1)
            
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]            
            triangle.append(row)
        
        return triangle
        # return list[list] 
    
    
solution = Solution()
print(solution.generate(5))