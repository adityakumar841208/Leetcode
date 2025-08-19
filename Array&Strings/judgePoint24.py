class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    
                    # remaining numbers after picking i and j
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    
                    a, b = nums[i], nums[j]
                    
                    for val in [a + b, a - b, b - a, a * b]:
                        if solve(next_nums + [val]):
                            return True
                    
                    if abs(b) > 1e-6 and solve(next_nums + [a / b]):
                        return True
                    
                    if abs(a) > 1e-6 and solve(next_nums + [b / a]):
                        return True
            return False
        
        # convert to float
        return solve([float(x) for x in cards])
        

solution = Solution()
print(solution.judgePoint24([4, 1, 8, 7]))  # ✅ True
