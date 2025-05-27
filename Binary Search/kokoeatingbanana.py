from math import ceil

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)  # Possible range for k
        
        while left < right:
            mid = (left + right) // 2  # Middle value of k
            total_hours = sum(ceil(pile / mid) for pile in piles)
            
            if total_hours <= h:
                right = mid  # Try a smaller k
            else:
                left = mid + 1  # Increase k
        
        return left  # The minimum valid k

# Test case
solution = Solution()
print(solution.minEatingSpeed([3,6,7,11], 8))  # Output: 4