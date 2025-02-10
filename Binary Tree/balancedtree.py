class Solution:
    def isBalanced(self, root):
        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            # If any subtree is unbalanced, return -1
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  # This signals imbalance
            
            return max(left_height, right_height) + 1

        return height(root) != -1  # If -1 is returned, the tree is unbalanced
