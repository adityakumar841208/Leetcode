class Solution:
    def numEquivDominoPairs(self, dominoes):
        hash_map = {}
        count = 0
        
        for domino in dominoes:
            # Sort the domino to ensure (a, b) and (b, a) are treated the same
            key = tuple(sorted(domino))
            if key in hash_map:
                count += hash_map[key]
                hash_map[key] += 1
            else:
                hash_map[key] = 1
                
        return count
               
            

solution = Solution()
print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))  # Output: 1