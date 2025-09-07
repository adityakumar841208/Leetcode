class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        res = 0
        
        while True:
            
            num = num1 - num2 * res
            
            if num < 0:
                return -1
            
            
            if bin(num).count("1") <= res and res <= num:
                return res
            
            res += 1
            
            
        return -1
            
    
    
solution = Solution()
print(solution.makeTheIntegerZero(3, -2))