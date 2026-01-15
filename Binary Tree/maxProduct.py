# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root):

        # return two parts max product
        self.maxProd = float('-inf')
        totalSum = 0

        # first get all sum 
        def getTotal(root):

            if not root:
                return 0
            
            leftSubTree = getTotal(root.left)
            rightSubTree = getTotal(root.right)
            total = root.val + leftSubTree + rightSubTree

            self.maxProd = max(self.maxProd, (totalSum - total) * total)

            return total
        
        totalSum = getTotal(root)
        getTotal(root)


        return self.maxProd


