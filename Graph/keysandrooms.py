class Solution:
    def canVisitAllRooms(self, rooms):
        
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
                    
        visited = set()
        dfs(0)
        return len(visited) == len(rooms)