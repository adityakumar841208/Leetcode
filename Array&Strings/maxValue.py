class Solution:
    def maxValue(self, events, k):
        max_sum = 0
        
        sorted_events = sorted(events,key=lambda x: x[0]) #Sort by first element
        visited = [0] * len(sorted_events)
        
        for i in range(len(sorted_events) -1):
            count = 0
            
            if sorted_events[i][1] >= sorted_events[i+1][0]:
                if sorted_events[i][2] > sorted_events[i+1][2] and visited[i] == 0:
                    visited[i] = 1
                    count += sorted_events[i][2]
                elif sorted_events[i][2] < sorted_events[i+1][2] and visited[i+1] == 0:
                    visited[i+1] = 1
                    count += sorted_events[i+1][2]
            print('Hey this is count number', count)
            max_sum += count
        
        return max_sum 
    
    
solution = Solution()
print(solution.maxValue([[1,1,1],[2,2,2],[3,3,3],[4,4,4]],3))