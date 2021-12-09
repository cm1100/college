board = {}

for i in range(9):
    board[i+1]=' '

print(board)


def peint_board(board):
    for i in range(1,10,3):
        print(f' {board[i]} | {board[i+1]} | {board[i+2]}')
        if i==7:continue
        print(" -------")

peint_board(board)

def pos_free(board,pos):
    print(pos)
    print(board)
    if board[pos]==' ':
        return True
    else:
        return False


def check_Draw(board):
    for key in board.keys():
        if board[key]==' ':
            return False
    return True

def checkWin(board):
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def insert_letter(letter,board,pos):


    if pos_free(board,pos):
        board[pos]=letter
        peint_board(board)

        if check_Draw(board):
            print("Draw")
            exit()

        if checkWin(board):
            if letter=='X':
                print("Bot wins")
            else:
                print("Player wins")




    else:
        print("cant print here")
        position = input("Enter new position")
        insert_letter(letter,board,int(position))


#insert_letter('X',board,2)

player='0'
bot = 'X'
def player_play(board):
    pos = input("Enter the position for '0': ")
    insert_letter(player,board,int(pos))
    return board

def computer_play(board):
    pos = input("Enter the position for 'X': ")
    insert_letter(bot, board, int(pos))
    return board

peint_board(board)




def comp_move(board):

    bestScore=-1000
    bestMove =0

    for key in board.keys():
        if (board[key]==" "):
            board[key]=bot
            score = minimax(board,0,False)
            board[key]=" "
            if score>bestScore:
                bestScore=score
                bestMove=key


    insert_letter(bot,board,bestMove)



def checkWin1(board,mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] ==mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False



def minimax(board,depth,isMaximizing):
    if checkWin1(board,bot):
        return 100
    elif checkWin1(board,player):
        return -100

    elif check_Draw(board):
        return 0

    if isMaximizing:

        bestScore = -1000


        for key in board.keys():
            if (board[key] == " "):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = " "
                if score > bestScore:
                    bestScore = score



        return bestScore

    else:
        bestScore = 1000

        for key in board.keys():
            if (board[key] == " "):
                board[key] = bot
                score = minimax(board, depth+1, False)
                board[key] = " "
                if score < bestScore:
                    bestScore = score

        return bestScore


while not checkWin(board):
    board=comp_move(board)
    board = player_play(board)





