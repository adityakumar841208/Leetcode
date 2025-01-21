class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


sum = ''
maxarr = 0
a = 'abcabcbb'
for char in a:
    if char not in sum:
        sum += char
    else:
        sum1 = sum[sum.index(char)+1:] + char
        sum2 = char
        # sum = max(len(sum1),len(sum2))
        if len(sum1) > len(sum2):
            sum = sum1
        else:
            sum = sum2

    maxarr = max(maxarr,len(sum))

print(maxarr)