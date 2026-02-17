class Solution:
    def readBinaryWatch(self, turnedOn):
        
        times = []

        for HH in range(12):
            for MM in range(60):
                if HH.bit_count() + MM.bit_count() == turnedOn:
                    if MM < 10:
                        MM = str(0) + str(MM)
                    times.append(f"{HH}:{MM}")

        return times
    
solution = Solution()
print(solution.readBinaryWatch(1))