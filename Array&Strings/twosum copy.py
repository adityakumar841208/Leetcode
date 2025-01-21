class Solution:
    def twoSum(self, nums, target):
        
        seen = []
        for index,data in enumerate(nums):
            diff = target - data
            if diff in seen:
                print(seen)
                return index, nums.index(diff)
            else:
                seen.append(data)
        print(seen)
        return None
    
nums = [2,7,11,15]
solution = Solution()
result = solution.twoSum(nums, 9)
print(result)

