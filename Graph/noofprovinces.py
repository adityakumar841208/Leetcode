class Solution:
    def findCircleNum(self, isConnected): 
        # [[1,1,0],[1,1,0],[0,0,1]] = 2
        
        def dfs(city):
            visited.add(city)
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and i not in visited:
                    dfs(i)
                    
        visited = set()
        provinces = 0
        for city in range(len(isConnected)):
            if city not in visited:
                provinces += 1
                dfs(city)
                
        return provinces
    
    
        
        
                
        