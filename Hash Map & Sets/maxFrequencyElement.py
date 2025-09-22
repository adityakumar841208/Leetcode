class Solution:
    def maxFrequencyElements(self, nums):
        
        nums_count = {}

        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        max_count = max(nums_count.values())
        return sum(count for count in nums_count.values() if count == max_count)