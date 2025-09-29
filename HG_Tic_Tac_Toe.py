''' Hi, My name is Hitika Ghanani and below is the code for a very popular game 'TIC TAC TOE'. 
I have build this game as a part of programming project. It was fun for me to build it and i hope 
you will also have fun playing it. So basically in this game two player play it from the same 
keyboard in a 3x3 grid and each player get turn alternately. One player uses X and the other 
player uses O. If any player gets 3 consecutive X's or O's be it horizontally or vertically or diagonally that player wins.
'''

#creating an empty 3x3 board
def resetBoard():
    board= [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]
    return board
    
#getting board
def printBoard(board):
    print("------------------")
    print("|R\\C| 0 | 1 | 2 |")
    print("------------------")
    print("| 0 |", board[0][0], "|", board[0][1], "|", board[0][2], "|")
    print("------------------")
    print("| 1 |", board[1][0], "|", board[1][1], "|", board[1][2], "|")
    print("------------------")
    print("| 2 |", board[2][0], "|", board[2][1], "|", board[2][2], "|")
    print("------------------\n")


#checking if user has appropiate entry or not
def validateEntry(row,col,board):
    if (row <0 or row >2 or col <0 or col >2):
        print("Invalid entry: try again.")
        print("Row & column number must be either 0, 1, or 2.\n")
        return False
    
    if board[row][col] != " ":
        print("The cell is already taken.")
        print("Please make another selection.\n")

        return False
    return True


#checking if the board is full or some empty spaces are left
def checkFull(board):
    for row in board:
        if " " in row:
            return False
    return True

#To check which user won
def CheckWin(board,turn):
    for i in range(3):

    #checking row wise
        if board[i][0] == turn and board[i][1] == turn and board[i][2] == turn:
            return True

    #checking column wise
        if board[0][i] == turn and board[1][i] == turn and board[2][i] == turn:
            return True

    #checking diagonally
    if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
        return True
    
    if board[0][2] == turn and board[1][1] == turn and board[2][0] == turn:
        return True
    
    return False

# To check if whether game has ended or not
def CheckEnd(board,turn):
    if CheckWin(board,turn):
        print(turn +" IS THE WINNER!!!")
        return True
    
    if checkFull(board):
        print("DRAW! NOBODY WINS!")
        printBoard(board)
        return True
    return False

#Loop for Main game 
def playGame():
    while True:
        board= resetBoard()
        print("\nNew Game: X goes first.\n")
        currentPlayer= "X"
        printBoard(board)

        while True:
            print(currentPlayer + "'s turn.")
            print("Where do you want your " + currentPlayer + " placed?")
            print("Please enter row number and column number separated by a comma.")

            move = input()
            try:
                row,col = move.split(",")
                row= int(row)
                col= int(col)
                print("You have entered row #"+ str(row))
                print("\t   and column #"+str(col))

            except:
                print("Invalid input format. Try again.")
                continue
            
            if not validateEntry(row,col,board):
                continue
            
            board[row][col]= currentPlayer
            print("Thank you for your selection.")  
            printBoard(board)


            if CheckEnd(board,currentPlayer):
                break

            if currentPlayer=="X":
                currentPlayer="O"

            else:
                currentPlayer="X"

        again = input("Another game? Enter Y or y for yes.\n")
        if again.lower()!="y":
            print("Thank you for playing!")
            break

if __name__=="__main__":
    playGame()



