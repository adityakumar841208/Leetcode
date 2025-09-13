class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_count = 0
        vowel = 'aeiou'
        
        for char in s:
            if char in vowel:
                vowel_count += 1
        
        
        return True if vowel_count > 0 and vowel_count % 2 != 0 else False
    
    
    
solution = Solution()
print(solution.doesAliceWin('leetcoder'))