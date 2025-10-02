class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        res = numBottles

        pairs = numBottles // numExchange
        reminder = numBottles % numExchange

        res += pairs

        while (pairs + reminder) // numExchange > 0:

            curr = (pairs + reminder) // numExchange

            reminder = (pairs + reminder) % numExchange
            pairs = curr
            res += curr

        return res

solution = Solution()
print(solution.numWaterBottles(9, 3))