class Solution:
    def smallestSubsequence(self, s):
        
        lastSeen = {}
        seen = {s[0]}
        ans = [s[0]]

        for index, char in enumerate(s):
            lastSeen[char] = index

        print(lastSeen)

        for i in range(1,len(s)):

            if s[i] > ans[-1] and s[i] not in seen:
                ans.append(s[i])
                seen.add(s[i])
            else:
                while ans and ans[-1] > s[i] and lastSeen[ans[-1]] > i:
                    char = ans.pop()
                    seen.remove(char)

                if s[i] not in seen:
                    ans.append(s[i])
                    seen.add(s[i])

        return "".join(ans)
    
solution = Solution()
print(solution.smallestSubsequence("cbaacabcaaccaacababa"))



        
        