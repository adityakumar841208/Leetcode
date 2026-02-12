class Solution:
    def longestBalanced(self, s: str) -> int:
        maxLen = 0
        n = len(s)
        for i in range(n):
            hashMap = {}

            for j in range(i, n):
                hashMap[s[j]] = hashMap.get(s[j], 0) + 1
                flag = True
                # iterate each of the hashmap list
                for key, value in hashMap.items():
                    if value != hashMap[s[j]]:
                        flag = False
                        break

                if flag:
                    maxLen = max(maxLen, j - i + 1)
        
        return maxLen

solution = Solution()
print(solution.longestBalanced('zzabccy'))