class Solution:
    def closeStrings(self,word1, word2):
        if set(word1) != set(word2):
            return False
        
        freq1 = {}
        freq2 = {}

        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1

        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1
            
        print('freq1',freq1)
        print('freq2',freq2)

        return sorted(freq1.values()) == sorted(freq2.values())

        
        
        
solution = Solution()
print(solution.closeStrings('cabbba','abbccc'))