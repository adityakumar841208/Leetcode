class Solution:
    def generate(self, numRows):
        
        # will start from top down approach
        dp = [[]] * numRows
        
        def findSol(n, memo):
            if n == 1:
                return [n]
            
            if n == 2:
                return [[1][1,1]]
            
            if n in memo:
                return n
            
            memo[n] = [findSol(n-1,memo),findSol(n-2,memo)]
            
            return memo
        
        findSol(numRows,dp)
        
        return dp
        
        # return list[list] 
    
    
solution = Solution()
print(solution.generate(5))