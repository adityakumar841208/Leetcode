class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        # count max freq of vowel 
        vowel_freq = {}
        consonant_freq = {}
        
        vowel = 'aeiou'
        
        for char in s:
            if char in vowel:
                vowel_freq[char] = vowel_freq.get(char, 0) + 1
            else:
                consonant_freq[char] = consonant_freq.get(char, 0) + 1
                
                
        return max(vowel_freq.values(), default=0) + max(consonant_freq.values(), default=0)
        
    
solution = Solution()
print(solution.maxFreqSum("abracadabra"))