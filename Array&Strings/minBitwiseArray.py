class Solution:
    def minBitwiseArray(self, nums):
        res = []

        for num in nums:
            if num == 2: 
                res.append(-1)
                continue
            
            bit = 0
            while (num >> bit) & 1:
                bit += 1
            
            if bit > 0:
                x = num ^ (1 << (bit - 1))
                res.append(x)
            else:
                res.append(-1)

        return res