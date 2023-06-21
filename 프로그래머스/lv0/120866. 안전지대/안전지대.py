# 위아래좌우대각선(시계방향)

nx = [-1,1,0,0,-1,-1,1,1] 
ny = [0,0,-1,1,-1,1,1,-1]

def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    x = i + nx[k]
                    y = j + ny[k]
                    if 0<=x<n and 0<=y< n:
                        if board[x][y] != 1:
                            board[x][y] = 2
    print(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    
    return answer