from math import isqrt

class Solution:
    def sumFourDivisors(self, nums):
        result = 0

        for num in nums:
            divisors = []

            for i in range(1, isqrt(num) + 1):
                if num % i == 0:
                    divisors.append(i)
                    if i != num // i:
                        divisors.append(num // i)

            if len(divisors) == 4:
                result += sum(divisors)

        return result


solution = Solution()
print(solution.sumFourDivisors([21, 4, 7]))  # 32
