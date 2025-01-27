class Solution:
    def equalPairs(self, grid) -> int:
        cols = {}
        counter = 0
        
        # Step 1: Store columns as tuples in the hash map
        for j in range(len(grid[0])):  # Iterate over columns
            col_tuple = tuple(grid[i][j] for i in range(len(grid)))  # Create column tuple
            cols[col_tuple] = cols.get(col_tuple, 0) + 1  # Count occurrences of each column
    
        # Step 2: Compare each row (as tuple) with the hash map
        for row in grid:
            row_tuple = tuple(row)  # Convert the row to a tuple
            counter += cols.get(row_tuple, 0)  # Add the count of matching columns
        
        return counter

# Example Usage
solution = Solution()
print(solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # Output: 1
