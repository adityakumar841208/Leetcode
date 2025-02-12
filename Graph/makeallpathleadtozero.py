from collections import defaultdict

class Solution:
    def minReorder(self, n, connections):
        self.rev = 0
        
        roads = set()
        graph = defaultdict(list)
        
        for u,v in connections:
            roads.add((u,v))
            
            graph[u].append(v)
            graph[v].append(u)
        
        print('graph = ',graph)
        print('roads =',roads)
        def dfs(u,parent):
            self.res += (parent,u) in roads
            
            for node in graph[u]:
                if parent == node:
                    continue
                dfs(node,parent)
        
        dfs(0,-1)
        return self.rev
        
        
solution = Solution()
solution.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]])
# [[0,1],[1,3],[2,3],[4,0],[4,5]]
# n = 6