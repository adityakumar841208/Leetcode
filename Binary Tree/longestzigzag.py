# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root):
        count = 0
        
        def dfs(root,direction,length):
            if not root:
                return
            
            count = max(count,length)
            
            if direction == 'left':
                dfs(root.right,'right',length+1)
                dfs(root.left,'left',length)
            else:
                dfs(root.left,'left',length+1)
                dfs(root.right,'right',length)
        
        dfs(root.left,'left',1)
        dfs(root.right,'right',1)
        
        return count