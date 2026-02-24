from math import sqrt
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        numsCount = 0

        def isPrime(n):

            limit = int(sqrt(n))
            for i in range(2, limit+1):
                if n % i == 0:
                    return False
                
            return True
        
        for i in range(left, right+1):
            bitCount = i.bit_count()

            if bitCount == 1:
                continue

            if isPrime(bitCount):
                numsCount += 1

        return numsCount

                

solution = Solution()
print(solution.countPrimeSetBits(10, 15)) # Output: 4