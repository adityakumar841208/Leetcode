
from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1] * len(rains)
        lake_map = {}
        dry_days = [] 

        for i, rain in enumerate(rains):
            if rain == 0:
                dry_days.append(i)
                res[i] = 1
            else:
                if rain in lake_map:
                    last_rain_day = lake_map[rain]
                    idx = bisect_right(dry_days, last_rain_day)
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days.pop(idx)
                    res[dry_day] = rain
                lake_map[rain] = i

        return res


solution = Solution()
print(solution.avoidFlood([1,2,0,1,2]))