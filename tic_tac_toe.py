def is_solved(board):

    for row in board:
        if row == [1, 1, 1]:
            return 1
        elif row == [2, 2, 2]:
            return 2

    for col in range(3):
        if [row[col] for row in board] == [1, 1, 1]:
            return 1
        elif [row[col] for row in board] == [2, 2, 2]:
            return 2

    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2

    if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        return 1
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        return 2

    for i in board:
        for j in i:
            if j == 0:
                return -1
    return 0
