from math import gcd
class Solution:
    def gcdSum(self, nums):
        prefixGcd = []
        prevMax = 0
        n = len(nums)
        ans = 0

        for i in range(n):

            if nums[i] > prevMax:
                prevMax = nums[i]

            prefixGcd.append(gcd(nums[i], prevMax))

        j = n - 1
        prefixGcd.sort()
        
        for i in range((n //2) + 1):
            if j != i and j > i:
                ans += gcd(prefixGcd[i], prefixGcd[j])
                j -= 1

        return ans
            
solution = Solution()
print(solution.gcdSum([6, 6]))

            
