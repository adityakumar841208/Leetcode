class Solution:
    def solveSudoku(self, board):
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empties = []  # list of empty cells to fill

        # Initialize sets with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)
                else:
                    empties.append((i, j))

        def solve(idx=0):
            if idx == len(empties):  # all cells filled
                return True

            i, j = empties[idx]
            box_index = (i // 3) * 3 + (j // 3)

            for val in map(str, range(1, 10)):
                if (val not in rows[i] 
                    and val not in cols[j] 
                    and val not in boxes[box_index]):

                    # Place value
                    board[i][j] = val
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box_index].add(val)

                    if solve(idx + 1):
                        return True

                    # Backtrack
                    board[i][j] = '.'
                    rows[i].remove(val)
                    cols[j].remove(val)
                    boxes[box_index].remove(val)

            return False

        solve()
                            
                        
        