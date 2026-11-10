def create_board():
    board = [None, None, None, None, None, None, None, None, None]
    return board


def print_board(board):
    for row in range(3):
        first = row * 3 
        
        cell1 = board[first] if board[first] else " "
        cell2 = board[first + 1] if board[first + 1] else " "
        cell3 = board[first + 2] if board[first + 2] else " "
        
        print(f"[{first + 1}] {cell1} | [{first + 2}] {cell2} | [{first + 3}] {cell3}")
        if row < 2:
            print("------+-------+------")








            
"""board = create_board()

print_board(board)

board[4] = "X"

print()
print_board(board)"""