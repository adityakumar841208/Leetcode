# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        
        if root is None:
            return 0 
    
        # Recursively find the max depth of the left and right subtrees, then add 1 for the current node
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1