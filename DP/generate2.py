class Solution:
    def generate(self, numRows):
        # dp - top down approach
        traingle = []
        
        for i in range(numRows):
            
            curr_row = [1] * (i+1)
            
            for j in range(1,i):
                curr_row[j] = traingle[i-1][j-1] + traingle[i-1][j]
                
            traingle.append(curr_row)
        
        return traingle
        
    
    
solution = Solution()
print(solution.generate(5))  # Example usage, should print the first 5 rows of