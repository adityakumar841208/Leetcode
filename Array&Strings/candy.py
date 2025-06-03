from collections import defaultdict

class Solution:
    def candy(self, ratings):
        candy = 0
        n = len(ratings)
        temp = [1]* n
        
        for i in range(n-1):
            if ratings[i] > ratings[i+1]:
                temp[i] = max(temp[i], temp[i+1]+1)
                
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i-1]:
                temp[i] = max(temp[i], temp[i-1]+1)
                
        for item in temp:
            candy += item
        
        return candy
    
solution = Solution()
print(solution.candy([1,2,2]))  # Example input to test the function
# output - 5 (1 + 2 + 2)