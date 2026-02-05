class Solution:
    def minimumPairRemoval(self, nums):
        opr = 0

        # Helper to check if array is sorted
        def is_sorted(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        while len(nums) > 1 and not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            # Find adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    idx = i

            # Remove the pair
            nums[idx] = nums[idx] + nums[idx + 1]
            nums.pop(idx + 1)

            opr += 1

        return opr



solution = Solution()
print(solution.minimumPairRemoval([5,2,3,1]))  # Example test case