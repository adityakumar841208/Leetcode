class Solution:
    def possibleStringCount(self, word):
        count = 0
        
        for i in range(1,len(word)):

            if word[i] == word[i-1]:
                print('word[i] = ', word[i], 'word[i-1] = ', word[i-1])
                count += 1
        
        return count + 1
    
solution = Solution()
print(solution.possibleStringCount('aaaa'))