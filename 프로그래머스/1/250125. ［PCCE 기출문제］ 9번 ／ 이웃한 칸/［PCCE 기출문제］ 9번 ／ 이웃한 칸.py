def solution(board, h, w):
    answer = 0
    n = len(board)
    for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
        nx, ny = dx+h, dy+w
        if 0<=nx<n and 0<=ny<n :
            if board[nx][ny] == board[h][w]:
                answer+=1
    return answer