# class Solution:
#     def maxVowels(self, s, k):
#         vowel_count = self.vowel_count(s[:k])
#         max_vowel = vowel_count
                
#         for i in range(k,len(s)):
#             vowel_count += self.vowel_count(s[i]) - self.vowel_count(s[i-k])
#             max_vowel = max(max_vowel,vowel_count)
            
#         return max_vowel
    
#     def vowel_count(self,s):
#         vowels = ('a','e','i','o','u')
#         vowel_count = 0
#         for i in s:
#             if i in vowels:
#                 vowel_count += 1
#         return vowel_count       
                
#         return vowel_count
        
    
# solution = Solution()
# print(solution.maxVowels("leetcode",3))


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a','e','i','o','u']
        vowel_count = 0
        
        for i in range(k):
            if s[i] in vowel:
                vowel_count += 1
                
        max_vowel = vowel_count
        for i in range(k,len(s)):
            print('i = ',s[i])
            if s[i] in vowel and s[i-k] not in vowel:
                vowel_count = vowel_count + 1
            elif s[i] not in vowel and s[i-k] in vowel:
                vowel_count = vowel_count - 1
                
            print('vowel_count = ',vowel_count)
        
            max_vowel = max(max_vowel,vowel_count)
            
        return max_vowel
        
        
solution = Solution()
print(solution.maxVowels("aditya",3))