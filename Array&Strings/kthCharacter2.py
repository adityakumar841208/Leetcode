class Solution:
    def kthCharacter(self, k: int, operations):
        word = 'a'
        
        for op in operations:
            if op == 0:
                word += word
            else:
                temp = word
                for char in word:
                    temp += chr(ord(char) + 1)
                word += temp
        
        return word[k]
    
    
solution = Solution()
print(solution.kthCharacter(10, [0,1,0,1]))