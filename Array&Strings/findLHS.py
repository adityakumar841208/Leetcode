from collections import Counter
class Solution:
    def findLHS(self, nums):
        count = Counter(nums)
        res = 0

        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])

        return res
    
solution = Solution()
print(solution.findLHS([1,3,2,2,5,4]))  # Output: 5