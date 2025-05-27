class Solution:
    def findWordsContaining(self, words, x):
        return [index for index,word in enumerate(words) if x in word]

solution = Solution()
print(solution.findWordsContaining(["leet", "code"], "e"))
