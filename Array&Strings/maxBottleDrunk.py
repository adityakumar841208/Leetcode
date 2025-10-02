class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            res += 1
            numBottles -= numExchange - 1
            numExchange += 1
            
        return res