class Solution:
    def minDominoRotations(self, tops, bottoms):
        
        def check(x):
            top_rotations = bottom_rotations = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    top_rotations += 1
                elif bottoms[i] != x:
                    bottom_rotations += 1
            return min(top_rotations, bottom_rotations)

        rotations = check(tops[0])
        if tops[0] != bottoms[0]:
            rotations = min(rotations, check(bottoms[0]))
        return -1 if rotations == float('inf') else rotations
    
solution = Solution()
print(solution.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))