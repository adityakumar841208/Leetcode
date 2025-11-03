class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        n = len(colors)

        i = 0
        while i < n:
            j = i
            max_time = 0
            sum_time = 0

            # process group of same color to ensure no two adjacent balloons have same color
            while j < n and colors[j] == colors[i]:
                sum_time += neededTime[j]
                max_time = max(max_time, neededTime[j])
                j += 1

            # add time for removing all but one
            total_time += sum_time - max_time

            # move to next group
            i = j

        return total_time
