class Solution:
    def checkEqualPartitions(self, nums, target):
        def findSubSets(product, tar, visited):
            for i in range(len(nums)):
                if i not in visited:
                    num = nums[i]
                    new_prod = product * num

                    if new_prod > tar:
                        continue
                    
                    visited.add(i)
                    
                    if new_prod == tar:
                        # Check if the remaining elements also make a product == target
                        prod2 = 1
                        for j in range(len(nums)):
                            if j not in visited:
                                prod2 *= nums[j]
                        if prod2 == target:
                            return True
                    else:
                        if findSubSets(new_prod, tar, visited):
                            return True

                    visited.remove(i)  # backtrack
            return False
        
        n = len(nums)
        for i in range(n):
            visited = set()
            visited.add(i)
            if findSubSets(nums[i], target, visited):
                return True
        
        return False 
        
    
solution = Solution()
print(solution.checkEqualPartitions(nums = [3,1,6,8,4], target = 24))  # Example input to test the function
# partition the array into two subsets


#https://leetcode.com/contest/weekly-contest-452/problems/partition-array-into-two-equal-product-subsets/description/
