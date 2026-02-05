from collections import defaultdict
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w * 2))

        pq = [(0, 0)]   # (cost, node)
        dist = [float('inf')] * n
        dist[0] = 0

        while pq:
            cost, node = heapq.heappop(pq)

            if node == n - 1:
                return cost

            if cost > dist[node]:
                continue

            for nxt, w in graph[node]:
                new_cost = cost + w
                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    heapq.heappush(pq, (new_cost, nxt))

        return -1
    
    # implement dikstra algo
    #  first graph with u -> v ( with w weight)
    # iterate with the first queue
    # pull it and check if it's the one we were looking for
    # if it's not get all the neighbours and push them into the pq