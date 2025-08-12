class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        
        # fill the left most basket and keep track of each basket whether it is filled or not
        
        visited = [0] * len(fruits)
        count = 0
        
        
        for i in range(len(fruits)):
            for j in range(len(baskets)):
            
                # check condition that can the element filled here ?
                if fruits[i] <= baskets[j]:
                    if visited[j] == 0:
                        count += 1
                        visited[j] += 1
                        break
                        
        return len(fruits) - count
            

        
    
solution = Solution()
print(solution.numOfUnplacedFruits( [4,2,5], [3,5,4]))