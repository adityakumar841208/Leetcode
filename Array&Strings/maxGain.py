class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s: str, first: str, second: str, score: int) -> (str, int):
            stack = []
            total = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(c)
            return ''.join(stack), total

        res = 0
        # Remove the more valuable pair first
        if x > y:
            s, gain = remove_pairs(s, 'a', 'b', x)
            res += gain
            _, gain = remove_pairs(s, 'b', 'a', y)
            res += gain
        else:
            s, gain = remove_pairs(s, 'b', 'a', y)
            res += gain
            _, gain = remove_pairs(s, 'a', 'b', x)
            res += gain

        return res
                
    
solution = Solution()
print(solution.maximumGain("aabbaaxybbaabb",5, 4))