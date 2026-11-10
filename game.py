from board import create_board, print_board

def get_player_move(board, current_player):
    while True:
        choice = input(f"Player {current_player}, choose a call (1-9): ")
        
        if not choice.isdigit():
            print("Please enter a number between 1 and 9.")
            continue
        
        choice = int(choice)
        
        if choice < 1 or choice > 9:
            print("invalid cell. choose a number between 1 to 9!")
            continue
        
        index = choice - 1
         
        if board[index] is not None:
            print("this cell is already taken. try again.")
            continue
        
        return index
    
    
WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)]
    
def check_winner(board, current_player):
    for line in WINNING_LINES:
        first = line[0]
        second = line[1]
        third = line[2]

        if (board[first] == current_player and
            board[second] == current_player and
            board[third] == current_player):
            return True

    return False

def check_draw(board):
    for cell in board:
        if cell is None:
            return False

    return True


def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"
    
    


def play_game():
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)

        index = get_player_move(board, current_player)

        board[index] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = switch_player(current_player)