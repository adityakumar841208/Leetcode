class Solution:
    def successfulPairs(self, spells, potions, success):
        """Binary search to find successful pairs."""
        
        potions.sort()
        result = []
        
        for spell in spells:
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            result.append(len(potions) - left)
        
        return result
    
    
solution = Solution()
print(solution.successfulPairs([5,1,3], [1,2,3,4,5], 7))  # Example usage
# Note: The successfulPairs function is not implemented here. In a real scenario, it would be provided by the system.