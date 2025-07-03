class Solution:
    def kthCharacter(self, k):
        string = ''
            
        while len(string) < k:
            
            
            if string == '':
                string = chr(97)
            else:
                for char in string:
                    string += chr(ord(char) + 1)
                    
        # If the string is longer than k, we can return the k-th character
        if len(string) > k:
            return string[k-1]
        # If the string is exactly k characters long, return the k-th character
        elif len(string) == k:
            return string[k-1]
    
    
solution = Solution()
print(solution.kthCharacter(5))