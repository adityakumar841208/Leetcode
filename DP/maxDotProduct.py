class Solution:
    def maxDotProduct(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        memo = {}

        def Solve(arr1Index, arr2Index):

            # base case avoid index out of range
            if arr1Index >= m or arr2Index >= n:
                return float('-inf')
            
            if (arr1Index, arr2Index) in memo:
                memo[(arr1Index, arr2Index)]
            
            # four cases
            curr = nums1[arr1Index] * nums2[arr2Index]
            prod = curr + max( 0, Solve(arr1Index + 1, arr2Index + 1))

            firstCase = Solve(arr1Index + 1, arr2Index)
            secondCase = Solve(arr1Index, arr2Index + 1)

            memo[(arr1Index, arr2Index)] = max(curr, prod, firstCase, secondCase)

            return memo[(arr1Index, arr2Index)]
        
        
        return Solve(0, 0)


solution = Solution()
print(solution.maxDotProduct([2,1,-2,5],[3,0,-6]))