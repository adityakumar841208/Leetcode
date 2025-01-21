class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0

        for index,data in enumerate(nums):
            if data != 0:
                nums[index] , nums[pointer] = nums[pointer] , nums[index]
                pointer += 1
        print(nums)
            




solution = Solution()
solution.moveZeroes([0,1,0,3,12])