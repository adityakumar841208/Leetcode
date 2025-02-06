from collections import defaultdict

class Solution:
    def pathSum(self, root, targetSum):
        
        def dfs(node, curr_sum):
            if not node:
                return 0

            # Compute current prefix sum
            curr_sum += node.val #curr_sum = 10
            
            # Find the number of valid paths ending at this node
            count = prefix_sum[curr_sum - targetSum] # 10-8 = 2
            
            # Store the current prefix sum in the hashmap
            prefix_sum[curr_sum] += 1
            
            # Recur for left and right children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # Backtrack: Remove the current prefix sum to maintain correct path count
            prefix_sum[curr_sum] -= 1
            
            return count

        # Hashmap to store prefix sums and their frequencies
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # Base case to handle when a path itself equals targetSum

        return dfs(root, 0)
