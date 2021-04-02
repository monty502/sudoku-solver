def sudoku_solve(board):
  helper(board)
  for row in range(0, 9):
    for col in range(0, 9):
      if board[row][col] != 0:
        continue
        
      for digit in range(1, 10):
        if is_in_row(digit, board, row):
          continue
          
        if is_in_col(digit, board, col):
          continue
          
        if is_in_block(digit, board, row, col):
          continue
        
        board[row][col] = digit
        if sudoku_solve(board):
          return True
      
      board[row][col] = 0
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

def helper(board):
  for vector in board:
    print(vector)
  print()


board = [
    [0,0,0,7,0,0,3,0,1],
    [3,0,0,9,0,0,0,0,0],
    [0,4,0,3,1,0,2,0,0],
    [0,6,0,4,0,0,5,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,8,0,4,0],
    [0,0,6,0,2,1,0,5,0],
    [0,0,0,0,0,9,0,0,8],
    [8,0,5,0,0,4,0,0,0]]
 
sudoku_solve(board)
helper(board)