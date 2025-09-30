class Solution:
    def triangularSum(self, nums):
        # prev = nums

        # while len(prev) > 1:
        #     curr = [0] * (len(prev) - 1)

        #     for i in range(len(curr)):
        #         curr[i] = (prev[i] + prev[i+1]) % 10

        #     prev = curr

        # return prev[0]

        n = len(nums)

        for i in range(n, 1, -1):
            for j in range(i - 1):
                nums[j] = (nums[j] + nums[j + 1] ) % 10

        return nums[0]
        

solution = Solution()
print(solution.triangularSum([1,2,3,4,5]))