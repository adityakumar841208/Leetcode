from collections import defaultdict

class Solution:
    def minScore(self, n, roads):
        
        graph = defaultdict(list)

        for ci1, ci2, distance in roads:
            graph[ci1].append((ci2, distance))
            graph[ci2].append((ci1, distance))


        def dfs(node, score, visited):
            
            for destination, distance in graph[node]:
                score = min(score, distance)
                if destination not in visited:
                    visited.add(destination)
                    score = dfs(destination, score, visited)

            return score


        score = dfs(1, float('inf'), {1})
        return score

solution = Solution()
print(solution.minScore(n = 6, roads = [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]))