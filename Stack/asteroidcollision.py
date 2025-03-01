class Solution:
    def asteroidCollision(self, asteroids):
        
        stack = []
        
        for index,asteroid in enumerate(asteroids):
            
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                
        return stack
        
        
solution = Solution()
print(solution.asteroidCollision([5,10,-5]))