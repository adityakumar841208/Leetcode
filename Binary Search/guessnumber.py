# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:



class Solution:
    def guessNumber(self, n: int) -> int:
        """Binary search to find the picked number."""
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            result = self.guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def guess(self, num: int) -> int:
        """Mock guess function for testing."""
        # This is just a placeholder. In an actual implementation, this would be provided by the system.
        picked_number = 6
        if num < picked_number:
            return 1  # num is lower than the picked number
        elif num > picked_number:
            return -1  # num is higher than the picked number
        else:
            return 0  # num is equal to the picked number
    
solution = Solution()
print(solution.guessNumber(10))  # Example usage, replace with actual guess function
# Note: The guess function is not implemented here. In a real scenario, it would be provided by the system.