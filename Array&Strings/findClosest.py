class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx, dy = abs(x - z), abs(y - z)
        
        if dx == dy:
            return 0
        return 1 if dx < dy else 2
    
    
solution = Solution()
print(solution.findClosest(2, 7, 4))