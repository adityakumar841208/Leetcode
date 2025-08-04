# class Solution:
#     def totalFruit(self, fruits):
        
        # max_len = 0
        # curr_len = 0
        
        # for i in range(len(fruits)):
        #     visited = []
            
        #     for j in range(i, len(fruits)):
        #         # go until 2 unique nums
        #         if fruits[j] not in visited:
        #             visited.append(fruits[j])
                    
        #         if len(visited) <= 2:
        #             curr_len += 1
        #         else:
        #             break
            
        #         max_len = max(max_len, curr_len) 
        #     curr_len = 0        
        
        
        # return max_len
    
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits):
        
        fruits_map = defaultdict(int)
        count = 0
        left = 0
        
        for index,num in enumerate(fruits):
            
            fruits_map[num] += 1
                        
            if len(fruits_map) > 2:
                # remove the elem
                fruits_map[fruits[left]] -= 1
                if fruits_map[fruits[left]] == 0:
                    del fruits_map[fruits[left]]
                left += 1
            count = max(count, index - left + 1)
        
        return count
        
        
    
    
solution = Solution()
print(solution.totalFruit([1,2,3,2,2]))