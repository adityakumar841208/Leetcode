class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        string = ''
        
        for char in s:
            if char not in string:
                string += char
            else:
                sum1 = string[string.index(char) + 1 : ] + char
                sum2 = char
                
                if len(sum2) > len(sum1):
                    string = sum2
                else:
                    string = sum1
                    
            maxLen = max(maxLen, len(string))
        return maxLen