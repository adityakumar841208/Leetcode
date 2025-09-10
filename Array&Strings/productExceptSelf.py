class Solution:
    def productExceptSelf(self, nums):
        
        n = len(nums)
        left = []
        right = [0] * n
        
        mul1 = 1
        for num in nums:
            mul1 *= num
            left.append(mul1)
            
        mul1 = 1
        for i in range(n-1, -1, -1):
            mul1 *= nums[i]
            right[i] = mul1
            
        for i in range(n):
            if i == 0:
                continue
                
            if i == n-1:
                right[i] = left[i-1]
                continue
                
            right[i] = right[i+1] * left[i-1]
        
        return right
    
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))