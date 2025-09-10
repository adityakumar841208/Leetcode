class Solution:
    def minimumTeachings(self, n: int, languages, friendships):
        
        sadUsers = set()
        for u1, u2 in friendships:
            if not set(languages[u1-1]) & set(languages[u2-1]):
                sadUsers.add(u1)
                sadUsers.add(u2)
                
        if not sadUsers:
            return 0
        
        langCount = [0] * (n + 1)
        for user in sadUsers:
            for lang in languages[user - 1]:
                langCount[lang] += 1
                
        return len(sadUsers) - max(langCount)
        
        
solution = Solution()
print(solution.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))  # Output: 1