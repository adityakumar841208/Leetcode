class Solution:
    def longestBalanced(self, nums):
        maxLen = 0
        hashMap = {} # key: prefix sum, value: index
        cumSum = [0] * len(nums)

        for i in range(len(nums)):

            val = 1 if nums[i] % 2 == 0 else -1

            seen = - 1
            if nums[i] in hashMap:
                # already visited
                seen = hashMap[nums[i]]

            if seen != -1:
                for j in range(0, seen+1):
                    cumSum[j] -= 1

            for t in range(0, i + 1):
                cumSum[t] += val
                if cumSum[t] == 0:
                    maxLen = max(maxLen, i - t + 1)

            hashMap[nums[i]] = val

        return maxLen
    

solution = Solution()
print(solution.longestBalanced([3,2,2,5,4]))