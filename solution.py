def sudoku_solve(board):
  for row in range(0, 9):
    for col in range(0, 9):
      if board[row][col] == '.':
        continue
        
      print(row, col)
      ch = board[row][col]
      for digit in range(1, 10):
        ch = str(digit)
        if is_in_row(ch, board, row):
          continue
          
        if is_in_col(ch, board, col):
          continue
          
        if is_in_block(ch, board, row, col):
          continue
        
        board[row][col] = ch
        if sudoku_solve(board):
          return True
      
      board[row][col] = '.'
      return False
  
  return True


def is_in_row(ch, board, row):
  return ch in board[row]

def is_in_col(ch, board, col):
  for row in range(0, 9):
    if board[row][col] == ch:
      return True
    
  return False

def is_in_block(ch, board, row, col):
  row_start = 0 if row < 3 else 3 if row < 6 else 6
  col_start = 0 if col < 3 else 3 if col < 6 else 6
  
#  print(row_start, col_start)
  for r in range(row_start, row_start + 3):
    for c in range(col_start, col_start + 3):
      if board[r][c] == ch:
        return True
    
  return False


board = (
    (0,0,0,7,0,0,3,0,1),
    (3,0,0,9,0,0,0,0,0),
    (0,4,0,3,1,0,2,0,0),
    (0,6,0,4,0,0,5,0,0),
    (0,0,0,0,0,0,0,0,0),
    (0,0,1,0,0,8,0,4,0),
    (0,0,6,0,2,1,0,5,0),
    (0,0,0,0,0,9,0,0,8),
    (8,0,5,0,0,4,0,0,0))
 
print(board[0][3])
#sudoku_solve(board)