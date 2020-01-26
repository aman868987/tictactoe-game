#board layout
def print_board(board):
    print('\n'*25)

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[1] + '|' + board[2] + '|' + board[3])
#input from player
def player_input():
    mark = ''
    while mark != 'O' and mark != 'X':
        mark = input("player 1 choose 'X' or 'O'\n").upper()
    if mark=='O':
        return('O','X')
    else:
        return('X','O')
#placing the mark
def place_mark(board,mark,position):
    board[position]=mark
#check for win
def win_check(board,mark):
    return((board[1]==board[2]==board[3]==mark)or(board[4]==board[5]==board[6]==mark)or(board[7]==board[8]==board[9]==mark)
           or(board[1]==board[4]==board[7]==mark)or(board[2]==board[5]==board[8]==mark)
           or(board[9]==board[6]==board[3]==mark)or(board[1]==board[5]==board[9]==mark)
           or(board[7]==board[5]==board[3]==mark))
#chooing player
import random
def choose():
    flip=random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
       return 'player 2'

#checking space on board
def check_space(board,position):
    return board[position]==' '
#check for full board
def full_check(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True
#choosing position
def choose_position(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position=int(input("choose position (1-9)"))
    return position
def replay():
    choice=input("play again? type 'yes'or'no'")
    return choice=='yes'

#main
print("welcome to the TIC TAC TOE!!!\n")
while True:
    #play the game
    ##set everything up(board,whose first,choose mark)
    board=[' ']*10
    p1_mark,p2_mark = player_input()
    turn=choose()
    print(turn+' will go first')
    play_game=input("ready to play? 'y'or'n'")
    if play_game=='y':
        game_on=True
    else:
        game_on=False


    ##game play
    while game_on:
        if turn=='player 1':
            #show the board
            print_board(board)
            #choose position
            position=choose_position(board)
            #place the position
            place_mark(board,p1_mark,position)
            #check if won
            if win_check(board,p1_mark):
                print_board(board)
                print("PLAYER 1 HAS WON!!")
                game_on=False
            #check for tie
            else:
                if full_check(board):
                    print("WOOPS!! IT'S A TIE")
                    game_on=False
                else:
                    turn='player 2'
        else:
            # show the board
            print_board(board)
            # choose position
            position = choose_position(board)
            # place the position
            place_mark(board, p2_mark, position)
            # check if won
            if win_check(board, p2_mark):
                print_board(board)
                print("PLAYER 2 HAS WON!!")
                game_on = False
            # check for tie
            else:
                if full_check(board):
                    print("WOOPS!! IT'S A TIE")
                    game_on = False
                else:
                    turn = 'player 1'

    if not replay():
        break
    #break the loop


