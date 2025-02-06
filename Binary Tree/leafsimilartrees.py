class Solution:
    def leafSimilar(self, root1, root2):
        # Helper function to collect leaves using DFS
        def dfs(root):
            if not root:
                return []
            # If it's a leaf node, return its value
            if not root.left and not root.right:
                return [root.val]
            # Otherwise, return leaf values from both subtrees
            return dfs(root.left) + dfs(root.right)

        # Get the leaf value sequences from both trees
        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        # Compare the two leaf sequences
        return leaves1 == leaves2
