class Solution:
    def differenceOfSums(self, n, m):
        sum1 = 0
        sum2 = 0
        
        for i in range(1,n+1):
            if i%m != 0:
                sum1+= i
            else:
                sum2+= i
                
        return sum1 - sum2
    
    
solution = Solution()
print(solution.differenceOfSums(10,3))
# sum1 = 1,2,4,5,7,8,10 - 36
# sum2 = 1,2,3 - 6