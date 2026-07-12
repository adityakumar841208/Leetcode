class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        prefixSum = [0] * (n + 1)
        prefixCnt = [0] * (n + 1)
        prefixVal = [0] * (n + 1)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')

            prefixSum[i + 1] = prefixSum[i] + d
            prefixCnt[i + 1] = prefixCnt[i]
            prefixVal[i + 1] = prefixVal[i]

            if d:
                prefixCnt[i + 1] += 1
                prefixVal[i + 1] = (prefixVal[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            digit_sum = prefixSum[r + 1] - prefixSum[l]
            k = prefixCnt[r + 1] - prefixCnt[l]

            curr = (
                prefixVal[r + 1]
                - prefixVal[l] * pow10[k]
            ) % MOD

            ans.append(curr * digit_sum % MOD)

        return ans