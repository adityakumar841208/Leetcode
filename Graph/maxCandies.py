class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
            visited = set()
            available = set(initialBoxes)
            candyCount = 0

            def dfs(box):
                if box in visited or status[box] == 0:
                    return 0
                visited.add(box)
                res = candies[box]

                for key in keys[box]:
                    status[key] = 1
                    if key in available and key not in visited:
                        res += dfs(key)

                for contained in containedBoxes[box]:
                    available.add(contained)
                    if status[contained] == 1 and contained not in visited:
                        res += dfs(contained)

                return res

            for box in initialBoxes:
                candyCount += dfs(box)

            return candyCount 

    
# traverse through contained Boxes
# status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]

solution = Solution()
print(solution.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))