from collections import defaultdict

def countCompleteComponents(n, edges):

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, visited):
        visited[node] = True

        vertices = 1                  # current node
        degree_sum = len(graph[node]) # degree of current node

        for nei in graph[node]:
            if not visited[nei]:
                v, d = dfs(nei, visited)
                vertices += v
                degree_sum += d

        return vertices, degree_sum

    visited = [False] * n
    ans = 0

    for i in range(n):
        if visited[i]:
            continue

        vertices, degree_sum = dfs(i, visited)
        edges = degree_sum // 2

        if edges == vertices * (vertices - 1) // 2:
            ans += 1

    return ans


print(countCompleteComponents(
    6,
    [[0,1],[0,2],[1,2],[3,4],[3,5]]
))