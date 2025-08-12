class Solution:
    def numberOfWays(self, n, x):
        
        modulo = 10**9 + 7
        
        data_map = [[-1] * 301 for _ in range(301)]
        
        def solve(num, curr, x):
            
            if num == 0:
                return 1
            
            if num < 0:
                return 0
            
            currPow = curr ** x
            
            if currPow > num:
                return 0
            
            if data_map[num][curr] != -1:
                return data_map[num][curr]
            
            take = solve(num - currPow, curr + 1, x)
            skip = solve(num, curr+1, x)
            
            data_map[num][curr] = take + skip
            
            return data_map[num][curr] % modulo
            
        
        return solve(n, 1, x)
        
        
    
    
solution = Solution()
print(solution.numberOfWays(4, 1)) # op - 2