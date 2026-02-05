class Solution:
    def maxSumTrionic(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        
        # Initialize states with a very small number
        INF = float('inf')
        # A: First Up, B: Down, C: Second Up
        a = b = c = -INF
        ans = -INF
        
        for i in range(1, n):
            prev, cur = nums[i-1], nums[i]
            
            # Temporary variables for the next state (so updates don't interfere)
            next_a = next_b = next_c = -INF
            
            if cur > prev:
                # To be in State A (First Up):
                # Either continue an existing State A, or start fresh with (prev + cur)
                next_a = max(a + cur, prev + cur)
                
                # To be in State C (Second Up):
                # Either continue an existing State C, or transition from State B
                if b != -INF:
                    next_c = max(c + cur, b + cur)
                elif c != -INF:
                    next_c = c + cur
                    
            elif cur < prev:
                # To be in State B (Down):
                # Either continue an existing State B, or transition from State A
                if a != -INF:
                    next_b = max(b + cur, a + cur)
                elif b != -INF:
                    next_b = b + cur
            
            # Update global states
            a, b, c = next_a, next_b, next_c
            
            # Our final answer can only come from State C (the completed pattern)
            if c != -INF:
                ans = max(ans, c)
                
        return ans if ans != -INF else 0

# Test
solution = Solution()
print(solution.maxSumTrionic([0, -2, -1, -3, 0, 2, -1])) # Output matches video logic