import random
def add_value(board, rand):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if count == rand:
                board[i][j] = 1
                return board
            count += 1

def find_table(board):
    r, c = 0, 0
    for arr in board:
        for ele in arr:
            if ele == 1:
                return [r, c]
            c += 1
        else:
            c = 0
        r += 1
    return False

