''' Hi, My name is Hitika Ghanani and I have build this connect 4 game as a part of my programming project.
So this program allows two players to play from the same keyboard turn by turn while choosing their row and 
column to mark their move. After each turn there are several checks made such as if a player won or is the 
board full or is an invalid entry been done.A player can win by placing 4 X or 4 O's either horizontally or 
vertically or diagonally together.
'''
row = 6
col = 7


#creating an empty 7x6 board
def resetBoard():
    global board
    board= [[" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "]]

    return board
    
#getting board
def printBoard(board):
    print("| 6 |", board[5][0], "|", board[5][1], "|", board[5][2], "|", board[5][3], "|", board[5][4], "|", board[5][5], "|", board[5][6], "|")
    print("---------------------------------")
    print("| 5 |", board[4][0], "|", board[4][1], "|", board[4][2], "|", board[4][3], "|", board[4][4], "|", board[4][5], "|", board[4][6], "|")
    print("---------------------------------")
    print("| 4 |", board[3][0], "|", board[3][1], "|", board[3][2], "|", board[3][3], "|", board[3][4], "|", board[3][5], "|", board[3][6], "|")
    print("---------------------------------")
    print("| 3 |", board[2][0], "|", board[2][1], "|", board[2][2], "|", board[2][3], "|", board[2][4], "|", board[2][5], "|", board[2][6], "|")
    print("---------------------------------")
    print("| 2 |", board[1][0], "|", board[1][1], "|", board[1][2], "|", board[1][3], "|", board[1][4], "|", board[1][5], "|", board[1][6], "|")
    print("---------------------------------")
    print("| 1 |", board[0][0], "|", board[0][1], "|", board[0][2], "|", board[0][3], "|", board[0][4], "|", board[0][5], "|", board[0][6], "|")
    print("---------------------------------")
    print("|R/C| a | b | c | d | e | f | g |")
    print("---------------------------------\n")
	

def validateMove(board, move):
    # Map column letters to indices
    col_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6}

    if len(move) < 2:
        return None

    col_letter = move[0].lower()
    row_number = move[1]
    if not row_number.isdigit():
        return None

    row_index = int(row_number) - 1
    col_index = col_map.get(col_letter, -1)

    # Check if indices are within board and cell is empty
    if col_index == -1 or row_index < 0 or row_index > 5 or board[row_index][col_index] != " ":
        return None

    return (row_index, col_index)
def availablePosition(board):
    # Returns list of available positions
    cols = ['a','b','c','d','e','f','g']
    available = []
    for i, col in enumerate(cols):
        for row in range(6):
            if board[row][i] == " ":  # check for empty space
                available.append(f'{col}{row+1}')
                break  # only the lowest empty row in this column
    return available


			
def CheckWin(board, turn):
    # Horizontal
    for i in range(6): # i is number of rows
        for j in range(4): #j is number of columns
            if board[i][j] == turn and board[i][j+1] == turn and board[i][j+2] == turn and board[i][j+3] == turn:  #checking for row if 4 dots are together
                return True

    # Vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] == turn and board[i+1][j] == turn and board[i+2][j] == turn and board[i+3][j] == turn:  #checking for columns if 4 dots are together
                return True

    # Diagonal
    for i in range(6):
        for j in range(7):
            # checking for down-right diagonal
            if i <= 2 and j <= 3:
                if board[i][j] == turn and board[i+1][j+1] == turn and board[i+2][j+2] == turn and board[i+3][j+3] == turn:
                    return True
            # checking for up-right diagonal
            if i >= 3 and j <= 3:
                if board[i][j] == turn and board[i-1][j+1] == turn and board[i-2][j+2] == turn and board[i-3][j+3] == turn:
                    return True

    return False
	

#To check if the board is full or not
def CheckFull(board):
    for j in range(7):         #loop through all columns
        if board[5][j] == " ": #checking if any top cell is empty or not
            return False
        
    return True       

def checkEnd(board, turn):
    # if current player just won
    if CheckWin(board, turn):
        return True
    
    # if board is completely full (draw)
    if CheckFull(board):
        return True
    
    # otherwise, game is still going
    return False

# Function to play a game of Connect Four
def main():
    turn = "X"                 # X always starts
    gameOver = False
    board = resetBoard()       # initialize empty board

    while not gameOver:
        printBoard(board)      # display the board
        print(f"{turn}'s turn.")

        available = availablePosition(board)  # get all available positions
        print("Available positions are:", available)

        move = input("Please enter column-letter and row-number (e.g., a1): ").lower()

        # Parse input
        if len(move) < 2:
            print("Invalid input. Try again.\n")
            continue

        col_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6}
        col_letter = move[0]
        row_str = move[1:]

        if col_letter not in col_map or not row_str.isdigit():
            print("Invalid input. Try again.\n")
            continue

        col = col_map[col_letter]
        row = int(row_str) - 1

        # Check if the column is full or move is not at the correct lowest available row
        # Find the lowest empty row in this column
        
        lowest_row = None
        for r in range(6):
            if board[r][col] == " ":
                lowest_row = r
                break

        if lowest_row is None:
            print("Invalid move. Column is full.\n")
            continue

        if row != lowest_row:
            print(f"You must place at the lowest available row in column {col_letter}. Try again.\n")
            continue

        # Place the marker
        board[lowest_row][col] = turn
        print("Thank you for your selection.\n")



        # Check for win or draw
        if CheckWin(board, turn):
            printBoard(board)
            print(f"{turn} IS THE WINNER!!!")
            gameOver = True
        elif CheckFull(board):
            printBoard(board)
            print("It's a draw!")
            gameOver = True
        else:
            turn = "O" if turn == "X" else "X"

    # Ask if players want to play again
    again = input("Another game (y/n)? ")
    if again.lower() == 'y':
        main()
    else:
        print("Thank you for playing!")


# Run the game
if __name__ == "__main__":
    main()