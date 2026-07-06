class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)

        count = 1
        last = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][1] <= last:
                # covered
                continue

            count += 1
            last = intervals[i][1]

        return count


solution = Solution()
print(solution.removeCoveredIntervals([[1,4],[1,6],[2,8]]))