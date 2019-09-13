from IPython.display import clear_output
import random
import time

p1marker = ''
p2marker = ''
marker = ''
position = ''
def display_board(board):
    clear_output()
    print(board[7] + " | " + board[8] + " | " + board[9])
    print('--|---|--')
    print(board[4] + " | " + board[5] + " | " + board[6])
    print('--|---|--')
    print(board[1] + " | " + board[2] + " | " + board[3])

def player_input():
    global p1marker, p2marker,marker
    while marker != 'X' and marker != 'O' :
        print('########################################')
        marker = input('what marker do u want player 1 (X/O):').upper()
    if marker == 'X':
        p1marker = 'X'
        p2marker = 'O'
        print('Player 1 uses {} and player 2 uses {}'.format(p1marker,p2marker))

    else:
        p1marker = 'O'
        p2marker = 'X'
        print('Player 1 uses {} and player 2 uses {}'.format(p1marker, p2marker))
    print('########################################')
#player_input()
def place_marker(board, marker, position, turn):
        print('########################################\n' + turn + ' Turn')
        position = input('Where do you want to place the marker?: ')
        if board[int(position)] == ' ' :
            board[int(position)] = marker
        else :
            print("Wrong Move")

def win_check(board, marker):
    if board[1] == board[2] ==board[3] == marker or \
        board[4] == board[5] == board[6] == marker or \
            board[7] == board[8] == board[9] == marker or \
            board[1] == board[4] == board[7] == marker or \
            board[2] == board[5] == board[8] == marker or \
            board[3] == board[6] == board[9] == marker or \
            board[1] == board[5] == board[9] == marker or \
            board[7] == board[5] == board[3] == marker :

        return True

def choose_first():
    print('Choosing which player goes first')
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    if random.randint(0,1) == 0:
        print('Player 1 Goes First')
        print('########################################')
        return 'Player 1'
    else:
        print('Player 2 Goes first')
        print('########################################')
        return  'Player 2'

def full_board_check(board):
    if board[1] != ' ' and \
        board[2] != ' ' and \
        board[3] != ' ' and \
        board[4] != ' ' and \
        board[5] != ' ' and \
        board[6] != ' ' and \
        board[7] != ' ' and \
        board[8] != ' ' and \
        board[9] != ' ' :
            print('########################################\nIts a tie')
            return  True


def replay():
    return input('Do you want to play again?(Y/N): ').lower().startswith('y')


def player_choice():
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:


        return position


print('########################################\nWelcome to Tic Tac Toe!\n########################################')
moves = ['','1','2','3','4','5','6','7','8','9']
print('Board Controls')

display_board(moves)

while True:
    # Reset the board
    theBoard = [' '] * 10
    player_input()
    turn = choose_first()


    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice()
            place_marker(theBoard, p1marker, position,turn)

            if win_check(theBoard, p1marker):
                display_board(theBoard)
                print('Player 1 has Won!\n########################################')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!\n########################################')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice()
            place_marker(theBoard, p2marker, position,turn)

            if win_check(theBoard, p2marker):
                display_board(theBoard)
                print('Player 2 has won!\n########################################')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!\n########################################')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break






