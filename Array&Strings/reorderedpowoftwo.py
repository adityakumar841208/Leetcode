from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count_n = Counter(str(n))
        
        for i in range(31):  # up to 2^30 (1,073,741,824)
            if count_n == Counter(str(1 << i)):
                return True
        return False

    
    
solution = Solution()
print(solution.reorderedPowerOf2(46))