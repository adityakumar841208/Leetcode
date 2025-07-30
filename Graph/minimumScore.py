from collections import defaultdict
class Solution:
    def minimumScore(self, nums, edges):
        
        res = 0
        n = len(nums)
        
        # store xor at all subtrees
        xor = [0] * n
        
        inTime = [0] * n
        outTime = [0] * n
        timer = 0
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent, path, xor, timer,inTime, outTime, node_values):
            xor[node] = nums[node]
            inTime[node] = timer
            timer += 1
            
            for connections in graph[node]:
                if connections != parent:
                    dfs(connections, node, path, xor, timer,inTime, outTime, node_values)
                    xor[node] ^= xor[connections]
                    
                
            outTime[node] = timer
            timer += 1
                         
        
        # get all xors excluding the parent
        dfs(0, -1, graph,xor,timer, inTime, outTime, nums )
        
        # count the number of edges that can be removed
        print(xor)            
        
        
        return res
    
    
solution = Solution()
print(solution.minimumScore( [1,5,5,4,11],[[0,1],[1,2],[1,3],[3,4]]))