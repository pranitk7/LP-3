
global N
N = 4
def isSafe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    return True

def SolveUtil(board, col):

    if col >= N:
        return True
    
    for i in range(N):

        if isSafe(board, i, col):
            board[i][col] = 1

            # Recur to place rest queens
            if SolveUtil(board, col+1) == True:
                return True
            

            board[i][col] = 0
    
    return False

if __name__ == '__main__':

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    
    SolveUtil(board, 0)

    print(board)