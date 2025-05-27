class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        # Find the length of the shortest common supersequence
        def lcs(str1, str2):
            n = len(str1)
            m = len(str2)
            dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if str1[i-1] == str2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[n][m]

        # Find the shortest common supersequence
        def scs(str1, str2):
            n = len(str1)
            m = len(str2)
            dp = [["" for _ in range(m+1)] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if str1[i-1] == str2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + str1[i-1]
                    else:
                        if len(dp[i-1][j]) > len(dp[i][j-1]):
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = dp[i][j-1]
            return dp[n][m]

        l = lcs(str1, str2)
        scs_str = scs(str1, str2)
        result = ""
        i = 0
        j = 0
        for ch in scs_str:
            while str1[i] != ch:
                result += str1[i]
                i += 1
            while str2[j] != ch:
                result += str2[j]
                j += 1
            result += ch
            i += 1
            j += 1
        result += str1[i:] + str2[j:]
        return result
        
        
solution = Solution()
print(solution.shortestCommonSupersequence("abac", "cab")) # "cabac"