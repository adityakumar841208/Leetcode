class Solution:
    def sumZero(self, n):
        
        arr = []
        start = (n+1) // 2
        
        prev = (start * -1)
       
        if n % 2 == 0:
            prev -= 1
            
        
        while len(arr) < n:
            
            curr = prev + 1

            if curr == 0 and n % 2 == 0:
                # even case
                curr += 1
            
            arr.append(curr)
            prev = curr
             
        
        return arr
    
    # optimized 
        # arr = []
        # for i in range(1, n // 2 + 1):
        #     arr.extend([i, -i])
        # if n % 2 == 1:
        #     arr.append(0)
        # return arr
    
    
solution = Solution()
print(solution.sumZero(1))