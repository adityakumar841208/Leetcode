class Solution:
    def replaceNonCoprimes(self, nums):
        
        res = []
        
        for num in nums:
            
            while res:
                from math import gcd
                g = gcd(res[-1], num)
                if g == 1:
                    break
                num = num * res.pop() // g
            res.append(num)
        
        return res
    
solution = Solution()
print(solution.replaceNonCoprimes([6,4,3,2,7,6,2]))  # [12,7,6]