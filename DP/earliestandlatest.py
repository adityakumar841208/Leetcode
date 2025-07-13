class Solution:
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        res = [1] * len(n)
        # will be using bit masking 
        
        def dfs(mask, player1, player2, round_num):
            if mask == (1 << n) - 1:
                return
            
            if player1 == player2:
                res[round_num] = min(res[round_num], player1)
                return 
            if player1 > player2:
                player1, player2 = player2, player1
            for i in range(n):
                if mask & (1 << i) == 0:
                    new_mask = mask | (1 << i)
                    dfs(new_mask, player1, player2, round_num + 1)
                    dfs(new_mask, player2, i + 1, round_num + 1)
            return

        dfs(0, firstPlayer - 1, secondPlayer - 1, 0)
        res = [x + 1 for x in res]
        
        return res
    
solution = Solution()
print(solution.earliestAndLatest(4, 1, 2))  # Example usage