board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
player = 'X'
move = 0

# printing the board
def print_board():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            
            if j<2:
                print(" | ", end='')
        print() 
        if i<2:
            print("---+---+--", end='') 
        print() 

def make_move():
    move = int(input(f"{player}, Please choose your move: "))
    pass

def update_board(move, player):
    cols, rows = 1, 2
    match move:
        case 1:
            rows, cols  = 0, 0
        case 2:
            rows, cols  = 0, 1
        case 3:
            rows, cols  = 0, 2
        case 4:
            rows, cols  = 1, 0
        case 5:
            rows, cols  = 1, 1
        case 6:
            rows, cols  = 1, 2
        case 7:
            rows, cols  = 2, 0
        case 8:
            rows, cols  = 2, 1
        case 9:
            rows, cols  = 2, 2
    if board[rows][cols] != 'X' and board[rows][cols] != 'O':
        board[rows][cols] = player
        return True
    else:
        return False
    
    







