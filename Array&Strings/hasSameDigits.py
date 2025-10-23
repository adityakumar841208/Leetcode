class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s) > 2:
            curr = ''
            for i in range(len(s) - 1):
                curr += str((int(s[i]) + int(s[i+1])) % 10)

            s = curr

        return True if s.count(s[0]) == 2 else False


solution = Solution()
print(solution.hasSameDigits("1234"))