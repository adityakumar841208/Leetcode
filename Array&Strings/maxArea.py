class Solution:
    def maxArea(self, height):
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            res = max(res, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

solution = Solution()
print(solution.maxArea([8,7,2,1]))  # ✅ Expected output = 49