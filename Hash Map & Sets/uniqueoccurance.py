class Solution:
    def uniqueOccurrences(self, arr):
        occurence = {}
        
        for i in arr:
            occurence[i] = occurence.get(i, 0) + 1
            print(occurence)
            # what does this line means is that if i is not in occurence then it will return 0 and add 1 to it
        
        return len(occurence.values()) == len(set(occurence.values()))


solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3])) # True