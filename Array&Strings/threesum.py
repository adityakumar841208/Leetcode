class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            data = nums[index]
            i, j = index + 1, len(nums) - 1

            while i < j:
                total = data + nums[i] + nums[j]
                if total == 0:
                    result.append([data, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif total < 0:
                    i += 1
                else:
                    j -= 1

        return result

solution = Solution()
ans = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(ans)
