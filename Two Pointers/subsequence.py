class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        if t == "" and s == "":
            return True
        
        for data in t:
            if i < len(s) and data == s[i]:
                i += 1
            if i == len(s):
                return True
        return False
            


solution = Solution()
print(solution.isSubsequence("",""))