from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    count = 1
    for row in board:
        if count == 1:
            print ("          C C C C C")
            print ("          1 2 3 4 5")
        print ("     Row"+str(count)+" " + " ".join(row))
        count += 1
player_one = input("Welcome Player one   What is your name? : ").upper()
player_two = input("Welcome Player two   What is your name? : ").upper()
print_board(board)

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board))

ship_row = random_row(board)
ship_col = random_col(board)
#Fill player name

# Everything from here on should go in your for loop!
turn = 1
for i in range(0, 10):

# Be sure to indent four spaces!
    if turn % 2 == 0:
        print ("***********"+player_two + "'s Turn***********")
    else:
        print ("***********"+player_one + "'s Turn***********")
    guess_row = int(input("***********Choose Row: "))
    guess_col = int(input("***********Choose Col: "))
    print ("")

    if guess_row-1 == ship_row and guess_col-1 == ship_col:
        print ("+++++++Congratulations! You sunk my battleship!+++++++++++")
        break
    else:
        if guess_row < 1 or guess_row > 5 or guess_col < 1 or guess_col > 5:
            print ("------Oops, that's not even in the ocean.-----")
            print (("-------------Try Again---------------"))
            turn -= 1
        elif(board[guess_row-1][guess_col-1] == "X"):
            print ("-----You guessed that one already.-----")
            print ("--------------Try Again---------------")
            turn -= 1
        else:
            print ("---You missed my battleship!---")
            board[guess_row-1][guess_col-1] = "X"
        
        print_board(board)
    turn += 1
    if turn == 10:
        print("")
        print ("----------------------Game Over----------------------")
        print("------------------------draw--------------------------")
        break