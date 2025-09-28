class Solution:
    def triangleNumber(self, nums) -> int:
        # if len(nums) < 3:
        #     return 0

        # count = 0
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         continue

        #     for j in range(i + 1, len(nums)):
                
        #         target = nums[i] + nums[j]
        #         k = bisect.bisect_left(nums, target, j + 1)
        #         count += k - (j + 1)

        # return count

        if len(nums) < 3:
            return 0
        
        count = 0
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] == 0:
                continue
            
            start = 0
            right = i - 1

            while start < right:
                if nums[start] + nums[right] > nums[i]:
                    count += right - start
                    right -= 1
                else:
                    start += 1    

        return count




solution = Solution()
print(solution.triangleNumber([2,2,3,4]))  # Output: 3