
from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1] * len(rains)  # Pre-fill with -1 for rainy days
        lake_map = {}  # Tracks last day each lake was filled
        dry_days = []  # Stores indexes of days when rain == 0

        for i, rain in enumerate(rains):
            if rain == 0:
                dry_days.append(i)
                res[i] = 1  # Default, will be updated later
            else:
                if rain in lake_map:
                    # We need to find a dry day *after* last rain of this lake
                    last_rain_day = lake_map[rain]
                    idx = bisect_right(dry_days, last_rain_day)
                    if idx == len(dry_days):
                        return []  # No available dry day → flood
                    dry_day = dry_days.pop(idx)
                    res[dry_day] = rain  # Use this dry day to dry that lake
                lake_map[rain] = i  # Update latest rain day

        return res


solution = Solution()
print(solution.avoidFlood([1,2,0,1,2]))