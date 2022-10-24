# this i

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board): # formatting the board to be printed like a sudoku board taken from the combination of lists above
    for e in range(len(board)): # prints a border under every third number to divide the grid of 9 numbers by using modulus to see if remainder equals zero 
        if e % 3 == 0 and e != 0: 
            print("- - - - - - - - - - - -")
        for f in range(len(board[0])): # same thing as the first one, although this one divided between the columns
            if f % 3 == 0 and f != 0:
                print(" | ", end = "")
            if f == 8: 
                print(board[e][f])
            else: 
                print(str(board[e][f]) + " ", end = "")

def find_empty_space(board): 
    for e in range(len(board)):
        for f in range(len(board[0])):
            if board[e][f] == 0: 
                return (e, f) # returns the row and the column of where a zero is located
    return None

def check(board,number,position):
    for e in range(len(board[0])): # this checks the rows
        if board[position[0]][e] == number and position[1] != e:
            return False
    for e in range(len(board)): # this checks the columns
        if board[e][position[1]] == number and position[0] != e: 
            return False
    box_1 = position[1] // 3 # each of these values return 0, 1, 2 indicating that it is either left, middle, or right (or top, middle and bottom)
    box_2 = position[0] // 3 
    for e in range(box_2*3, box_2*3 + 3): # this checks to see if the number already appears in this section of the board's 9 squares
        for f in range(box_1*3, box_1*3 + 3):
            if board[e][f] == number and (e,f) != position:
                return False
    return True

def solve(board):
    find = find_empty_space(board)
    if not find:
        return True # if there is no more empty spaces, or zeros, it returns True because the board is already solved
    else:
        row, col = find
    for e in range(1,10):
        if check(board, e, (row, col)):
            board[row][col] = e
            if solve(board):
                return True
            board[row][col] = 0 # 
    return False
