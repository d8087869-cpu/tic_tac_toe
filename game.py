def get_player(board, current_player):
    while True:
        choice = input(f"Player {current_player}, choose a call (1-9): ")
        if not choice.isdigit():
            print("Please enter a nimber between 1 and 9.")
            continue
        choice = int()
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