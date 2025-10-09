class Solution:
    def minTime(self, skill, mana):
        n = len(skill)
        m = len(mana)

        timeTaken = [0] * n


        # iterate through each of the potions -> mana
        for j in range(m):
            # initialize the timeTaken of first wizard
            timeTaken[0] += mana[j] * skill[0]
            for i in range(1, n):
                # getting the maximum between the maximum valid and previous data -> as 0 is already assigned
                timeTaken[i] = max(timeTaken[i-1], timeTaken[i])+ mana[j] * skill[i]
                
            # synchronize the timeTaken
            for t in range(n-1, 0, -1):
                timeTaken[t-1] = timeTaken[t] - mana[j] * skill[t]


        return timeTaken[n-1] # last value

solution = Solution()
print(solution.minTime([1,5,2,4], [5,1,4,2]))