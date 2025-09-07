class Solution:
    def minOperations(self, queries):
        res = 0
        
        def solve(left, right):
            l = 1
            s = 1
            steps = 0
            
            while l < right:
                r = l * 4 -1
                
                start = max(l, left)
                end = min(right, r)
                
                if start < end:
                    steps += (end - start + 1) * s
                
                s += 1
                l *= 4
            
            return steps
        
        for l, r in queries:
            
            steps = solve(l, r)
            
            res += (steps+1) // 2
            
        return res
    
solution = Solution()
print(solution.minOperations([[2,6]]))