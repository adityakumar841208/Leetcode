class Solution:
    def goodNodes(self, root):
        
        def dfs(root,max_val):
            if not root:
                return 0
            
            count = 1 if root.val >= max_val else 0  # Check if node is "good"
            
            max_val = max(max_val,root.val)
            
            count += dfs(root.left,max_val)
            count += dfs(root.right,max_val)
            
            return count
                 
        return dfs(root,root.val)