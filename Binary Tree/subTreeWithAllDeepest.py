# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root):
        

        def dfs(node):
            
            leftDepth, leftNode = dfs(node.left)
            rightDepth, rightNode = dfs(node.right)


            if leftDepth > rightDepth:
                return [leftDepth + 1, leftNode]
            elif rightDepth > leftDepth:
                return [rightDepth + 1, rightNode ]
            else:
                # both are same
                return [leftDepth + 1, node ]


        return dfs(root)[1]

