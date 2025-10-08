class Solution:
    def successfulPairs(self, spells, potions, success):
        res = []
        portions = sorted(potions)
        n = len(potions) - 1

        for item in spells:
            left = 0
            right = n

            while left <= right:
                mid = left + (right-left) // 2

                if item * potions[mid] >= success:
                    right = mid - 1
                elif item * potions[mid] < success:
                    left = mid + 1
            res.append(len(potions) - left)

        return res

solution = Solution()
print(solution.successfulPairs([5,1,3], [1,2,3,4,5], 7))
            
       