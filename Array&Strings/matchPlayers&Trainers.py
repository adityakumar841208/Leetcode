class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        
        # is there any edge case missing there ?
        if not players or not trainers:
            return 0
        
        # sort both lists
        players = sorted(players)
        trainers = sorted(trainers)
        
        res = 0
        i = 0
        j = 0
        
        while( i < len(players) and j < len(trainers)):
            if players[i] <= trainers[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return res
        
        
    
solution = Solution()
print(solution.matchPlayersAndTrainers([4,7,9],[8,2,5,8]))