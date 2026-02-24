class Solution:
    def sumRootToLeaf(self, root):
        res = 0

        def exploreTree(node, curr):
            nonlocal res

            curr += str(node.val)

            # leaf node
            if not node.left and not node.right:
                res += int(curr, 2)
                return

            if node.left:
                exploreTree(node.left, curr)
            if node.right:
                exploreTree(node.right, curr)

        exploreTree(root, "")
        return res