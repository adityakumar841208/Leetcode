class Solution:
    def isPalindrome(self, x: int) -> bool:
        data = str(x)
        if data == data[::-1]:
            return True
    
        return False

solution = Solution()
ans = solution.isPalindrome(-121)
print(ans)