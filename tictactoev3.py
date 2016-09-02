import random

grid = [["_", "_", "_"], ["_", "_", "_"], [" ", " ", " "]]


def print_grid(grid):
  for line in grid:
    print "|".join(line)

def check_if_won(grid, symbol):
  for row in range(3):
    if grid[row][0] == symbol and grid[row][1] == symbol and grid[row][2] == symbol:
      return True
      break
  for col in range(3):
    if grid[0][col] == symbol and grid[1][col] == symbol and grid[2][col] == symbol:
      return True
      break
  if grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
    return True
  if grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol:
    return True
  return False
  
def choose_square(symbol):
  row = int(raw_input("Place an %s!\nChoose a row:" % symbol)) - 1
  col = int(raw_input("Choose a column:")) - 1
  if check_square_free(grid, row, col) == True:
    return row, col
  else:
    print "Invalid square. Choose again."
    print_grid(grid)
    choose_square(symbol)

def check_if_full(grid):
  for row in range(3):
    for col in range(3):
      if check_square_free(grid, row, col) == True: 
        return False
  return True

def check_square_free(grid, row, col):
  return check_in_grid(row, col) == True and grid[row][col] != "X" and grid[row][col] != "O"

def check_for_symbol(grid, row, col, symbol):
  return check_in_grid(row, col) == True and grid[row][col] == symbol

def check_in_grid(row, col):
  return (-1 < row <= 2) and (-1 < col <= 2)

def fill_two(symbol, x, y):
  #This logic blocks two X's in a row, column or diagonal
  if grid[x][y] == symbol:
    #vertical
    if check_for_symbol(grid, x+1, y, symbol) == True:
      if check_square_free(grid, x+2, y) == True:
        row = x+2 
        col = y
        print 'vertical'
        return row, col
      elif check_square_free(grid, x-1, y) == True:
        row = x-1
        col = y
        print 'vertical'
        return row, col
    #horizontal
    if check_for_symbol(grid, x, y+1, symbol) == True:
      if check_square_free(grid, x, y+2) == True:
        row = x 
        col = y+2
        print 'horizontal'
        return row, col
      elif check_square_free(grid, x, y-1) == True:
        row = x
        col = y-1
        print 'horizontal'
        return row, col
    #diagonal
    if check_for_symbol(grid, x+1, y+1, symbol) == True:
      if check_square_free(grid, x+2, y+2) == True:
        row = x+2 
        col = y+2
        print 'diagonal 1'
        return row, col
      elif check_square_free(grid, x-1, y-1) == True:
        row = x-1
        col = y-1
        print 'diagonal 2'
        return row, col
    if check_for_symbol(grid, x+1, y-1, symbol) == True:
      if check_square_free(grid, x-1, y+1) == True:
        row = x-1 
        col = y+1
        print 'diagonal 3', x, y
        return row, col
      elif check_square_free(grid, x+2, y-2) == True:
        row = x+2
        col = y-2
        print 'diagonal 4'
        return row, col
    #horiz gap
    if check_square_free(grid, x, y+1) == True and check_for_symbol(grid, x, y+2, symbol) == True:
      row = x
      col = y+1
      print 'horizontal gap'
      return row, col
    #vertical gap
    if check_square_free(grid, x+1, y) == True and check_for_symbol(grid, x+2, y, symbol) == True:
      row = x+1
      col = y
      print 'vertical gap'
      return row, col
  return None


def computer_choose_square(symbol):
  print "Computer is choosing..."
  #Fill's in the gap if there are two O's
  for x in range(3):
    for y in range(3):
      if fill_two("O", x, y) is not None:
        print "Fill two O", fill_two("O", x, y)
        return fill_two("O", x, y)
      #Blocks two X's
      if fill_two("X", x, y) is not None:
        print "Fill two X", fill_two("X", x, y)
        return fill_two("X", x, y)
  #If computer has center, take a corner
  if check_for_symbol(grid, 1, 1, "O") == True:
    if check_square_free(grid, 0, 0) == True:
      row = 0
      col = 0
      return row, col
    elif check_square_free(grid, 0, 2) == True:
      row = 0
      col = 2
      return row, col
    elif check_square_free(grid, 2, 0) == True:
      row = 2
      col = 0
      return row, col
    elif check_square_free(grid, 2, 2) == True:
      row = 2
      col = 2
      return row, col
  #Grab the Center
  if check_square_free(grid, 1, 1):
    print "Center"
    row = 1
    col = 1
  #Take a Random Square
  else:
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    print "Random", row, col
    if check_square_free(grid, row, col) == False:
      return computer_choose_square(symbol)
  return row, col



#Program operating instructions down here

for turn in range(5):
  print_grid(grid)
  if check_if_full(grid) == True:
    print "Board is full. Game Over."
    break
  row, col = choose_square("X")
  grid[row][col] = "X"
  if check_if_won(grid, "X") == True:
    print_grid(grid)
    print "X's won!"
    break
  print_grid(grid)
  if check_if_full(grid) == True:
    print "Board is full. Game Over."
    break
  row, col = computer_choose_square("O")
  grid[row][col] = "O"
  if check_if_won(grid, "O") == True:
    print_grid(grid)
    print "O's won!"
    break


 
