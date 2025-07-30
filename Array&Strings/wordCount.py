class Solution:
    def wordCount(self, startWords, targetWords):
    
        start_set = set([''.join(sorted(word)) for word in startWords])
        res = 0
        
        print(start_set)

        for target in targetWords:
            sorted_target = ''.join(sorted(target))
            for i in range(len(sorted_target)):
                possible = sorted_target[:i] + sorted_target[i+1:]
                
                if possible in start_set:
                    res += 1
                    break

        return res

    
solution = Solution()
print(solution.wordCount(["ab","a"],["abc","abcd"]))