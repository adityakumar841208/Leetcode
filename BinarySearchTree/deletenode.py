# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root, key):
        
        def findMinNode(node):
            while node.left:
                node = node.left
            return node
        
        if not root:
            return None  # Corrected: Should return None, not an empty return
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  
            # Case 1: No child
            if not root.left and not root.right:
                return None  
            # Case 2: One child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: Two children
            else:
                minNode = findMinNode(root.right)  # Find the smallest node in the right subtree
                root.val = minNode.val  # Replace value with minNode's value
                root.right = self.deleteNode(root.right, minNode.val)  # Delete minNode
        
        return root
