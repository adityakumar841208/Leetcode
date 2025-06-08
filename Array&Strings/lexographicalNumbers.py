class Solution:
    def lexicalOrder(self, n):
        li = [''] * n
        
        for i in range(1,n+1):
            li[i-1] = i

        li = sorted(li, key=str)

        return li
    
    
solution = Solution()
print(solution.lexicalOrder(n = 13))