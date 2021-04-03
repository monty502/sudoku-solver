def sudoku_solve(board):
  helper(board)
  for row in range(9):
    for col in range(9):
      if board[row][col] != 0:
        continue
        
      for digit in range(1, 10):
        if digit in board[row]:
          continue
          
        if digit in (vector[col] for vector in board):
          continue
          
        if is_in_block(digit, board, row, col):
          continue
        
        board[row][col] = digit
        if sudoku_solve(board):
          return True
      
      board[row][col] = 0
      return False
  
  return True

def is_in_block(ch, board, row, col):
  row_start = 0 if row < 3 else 3 if row < 6 else 6
  col_start = 0 if col < 3 else 3 if col < 6 else 6
  
#  print(row_start, col_start)
  for r in range(row_start, row_start + 3):
    for c in range(col_start, col_start + 3):
      if board[r][c] == ch:
        return True
    
  return False

possibility = [[{} for _ in range(9)] for _ in range(9)]
def set_possibilities(board):
  # pass
  for row in range(9):
    for col in range(9):
      if board[row][col] != 0:
        continue

      all_digits = {i for i in range(1, 10)}
      for i in range(9):
        if board[row][i] in all_digits:
          all_digits.remove(board[row][i])
        if board[i][col] in all_digits:
          all_digits.remove(board[i][col])

        row_start = 0 if row < 3 else 3 if row < 6 else 6
        col_start = 0 if col < 3 else 3 if col < 6 else 6
        
        for r in range(row_start, row_start + 3):
          for c in range(col_start, col_start + 3):
            if board[r][c] in all_digits:
              all_digits.remove(board[r][c])

      # print(row, col, all_digits)
      possibility[row][col] = all_digits


def redraw(board):
  modified = False
  for row in range(9):
    for col in range(9):
      if len(possibility[row][col]) == 1:
        board[row][col] = possibility[row][col].pop()
        modified = True
        print(row, col, board[row][col])
        helper(board)
  return modified


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
 
while True:
  set_possibilities(board)
  helper(possibility)
  if not redraw(board):
    break


sudoku_solve(board)
helper(board)
'''
'''