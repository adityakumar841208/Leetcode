class Solution:
    def pushDominoes(self, dominoes):
        
        n = len(dominoes)
        left = [float('inf')] * n
        right = [float('inf')] * n

        time = float('inf')
        
        # Right force
        for i in range(n):
            if dominoes[i] == 'R':
                time = 0
            elif dominoes[i] == 'L':
                time = float('inf')
            else:
                if time != float('inf'):
                    time += 1
            right[i] = time

        time = float('inf')
        # Left force
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                time = 0
            elif dominoes[i] == 'R':
                time = float('inf')
            else:
                if time != float('inf'):
                    time += 1
            left[i] = time

        result = []
        for i in range(n):
            if left[i] == right[i]:
                result.append('.')
            elif left[i] < right[i]:
                result.append('L')
            else:
                result.append('R')
        return ''.join(result)

solution = Solution()
print(solution.pushDominoes("RR.L"))

