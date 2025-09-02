class Solution:
    def isValidSudoku(self, board):
        
        # validate each row
        for row in board:
            seen = set()
            for num in row:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
                    
        # validate each column
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
                
        def validateBox(box_row, box_col, board):
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = board[box_row * 3 + i][box_col * 3 + j]
                    if num != '.':
                        if num in seen:
                            return False
                        seen.add(num)
            return True 
                    
        # validate eaach 3x3 sub-box
        for box_row in range(3):
            for box_col in range(3):
                if not validateBox(box_row, box_col, board):
                    return False
                
        
        return True
    
    
solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                              ["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],
                              ["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],
                              ["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],
                              [".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]))  # Example usage