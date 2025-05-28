from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        n = len(edges1) + 1
        m = len(edges2) + 1

        res1 = [0] * n
        res2 = [0] * m

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        def bfs(source, k, graph):
            visited = set()
            queue = deque([(source, 0)])
            visited.add(source)
            count = 0

            while queue:
                node, dist = queue.popleft()
                if dist > k:
                    continue
                count += 1
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))
            return count

        for i in range(n):
            res1[i] = bfs(i, k, graph1)

        for i in range(m):
            res2[i] = bfs(i, k - 1, graph2)

        max_from_tree2 = max(res2)
        answer = [res1[i] + max_from_tree2 for i in range(n)]
        return answer

# Sample test
solution = Solution()
print(solution.maxTargetNodes(
    [[0,1],[0,2],[2,3],[2,4]],
    [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]],
    2
))
# Output should be: [9, 7, 9, 8, 8]
