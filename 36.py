table = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def check_valid_sudoku(board):
    boxes = {i:[] for i in range(9)}
    for i in range(9):
        row = []
        column = []
        for j in range(9):
            row_index, column_index = board[i][j], board[j][i]
            boxes_index = boxes[(j//3) + ((i//3)*3)]            
            
            if row_index in row or column_index in column or row_index in boxes_index: 
                return False
            else: 
                if row_index != '.':
                    row.append(row_index)
                    boxes_index.append(board[i][j])
                if column_index != '.':
                    column.append(column_index)
                
    return True

print(check_valid_sudoku(table))


lst = [[[0], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[1], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[2], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[3], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[4], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[5], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[6], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[7], 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [[8], 0, 1, 2, 3, 4, 5, 6, 7, 8]]

