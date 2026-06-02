class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        
        # min_time
        min_time = float('inf')
        # find duration of each task

        landArr = []
        waterArr = []

        for i in range(len(landStartTime)):
            landArr.append(landStartTime[i] + landDuration[i])

        for i in range(len(waterStartTime)):
            waterArr.append(waterStartTime[i] + waterDuration[i])

        # if overlap in time found add the greater duration one then for the secode task add their (lastDuration - start)

        for i in range(len(landArr)):
            for j in range(len(waterArr)):

                land_then_water = max(landArr[i], waterStartTime[j]) + waterDuration[j]

                water_then_land = max(waterArr[j], landStartTime[i]) + landDuration[i]

                min_time = min(min_time, land_then_water, water_then_land)

        return min_time

solution = Solution()
print(solution.earliestFinishTime([5], [3], [1], [10]))