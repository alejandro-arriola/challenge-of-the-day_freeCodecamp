def tic_tac_toe(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return f"{row[0]} wins"
    
    board = list(map(list, zip(*board)))
    
    for row in board:
        if row[0] == row[1] == row[2]:
            return f"{row[0]} wins"
    
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return f"{board[1][1]} wins"

    return "Draw"

print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]))