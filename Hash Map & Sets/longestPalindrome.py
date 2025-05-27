class Solution:
    def longestPalindrome(self, words):
        result = 0
        hash_map = {}
        
        for word in words:
            # check for the data is that in the set in the reverse order or not
            rev_word = word[::-1]
            if rev_word in hash_map and hash_map[rev_word] > 0:
                result += 4
                hash_map[rev_word] -= 1
            else:
                if word in hash_map:
                    hash_map[word] += 1
                else:
                    hash_map[word] = 1
                    
        # check for the middle element
        for word in hash_map:
            if word[0] == word[1] and hash_map[word] > 0:
                result += 2
                break
            
        return result
    
    
solution = Solution()
print(solution.longestPalindrome(["lc", "cl", "gg"]))  # Output: 6