from IPython.display import clear_output
import random

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    mark=''
    while not (mark == 'X' or mark =='O'):
        mark = input('Player 1: Do you want to be X or O? ').upper()
    if(mark == 'X'):
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'

def full_board(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True

def space_check(board,position):
    return board[position] == ' '

def player_choice(board):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    return input('Do you want to play. Yes/No').lower().startswith('y')

while True:
    theBoard =[' ']*10
    player_1,player_2 = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    player_input = input('Are you ready for the game. Yes/No')
    if player_input.lower()[0] =='y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if(turn=='Player 1'):
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player_1,position)
            if win_check(theBoard,player_1):
                display_board(theBoard)
                print('Congratulation,You have won!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_board(theBoard)
                    print('Game is a tie')
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player_2,position)
            
            if win_check(theBoard,player_2):
                display_board(theBoard)
                print('Congratulation,You have won!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_board(theBoard)
                    print('Game is a tie')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
