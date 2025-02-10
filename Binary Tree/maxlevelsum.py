from collections import deque

class Solution: 
    def maxLevelSum(self, root):
        if not root:
            return 0
        
        max_sum = float('-inf')
        max_level = 1
        level = 1
        queue = deque([root])
        
        while queue:
            curr_sum = 0
            temp = deque()
            for node in queue:
                curr_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right) 
            
            # Change '>' to '>=' to prioritize the deepest level
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = level
            
            queue = temp
            level += 1
        
        return max_level  # Return the highest (deepest) level with the max sum
