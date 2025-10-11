class Solution:
    def maximumTotalDamage(self, power):

        freq = {}
        for spellVal in power:
            freq[spellVal] = freq.get(spellVal, 0) + 1

        power = sorted(set(power)) # remove the duplicate and sort it
        n = len(power)
        dp = [-1] * n
        
        def exploreNode(index):
            if index >= n:
                return 0
            
            if dp[index] != -1:
                return dp[index]
            
            # calculate the val
            # add the frequency and then go for further calculation

            frequency_sum = freq[power[index]] * power[index]
            next_index = index + 1

            while next_index < n and power[next_index] <= power[index] + 2:
                next_index += 1

            # take 
            take = frequency_sum + (exploreNode(next_index))
            # skip
            skip = exploreNode(index+1)

            dp[index] = max(skip, take)
            return dp[index]

        # explore at each number for the maximum 
        return exploreNode(0)


solution = Solution()
print(solution.maximumTotalDamage([1,1,3,4]))