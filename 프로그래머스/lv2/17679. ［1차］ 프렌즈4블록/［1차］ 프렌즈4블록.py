from collections import deque
def solution(m, n, board):
    board = [[j for j in i ] for i in board]
    answer = 0
    dx = [0,0,1,1]
    dy = [0,1,0,1]

    
    # 4방향 확인
    def check(x,y):
        for k in range(4):
            nx, ny = dx[k] + x, dy[k] + y
            if 0<=nx<m and 0<= ny<n and board[x][y] != 1 and board[nx][ny] == board[x][y]:
                continue
            else:
                return False
        return True

    while True:
        v = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if check(i,j):
                    for k in range(4):
                        nx, ny = dx[k] + i, dy[k] + j
                        v[nx][ny] = 1
        tmp_cnt = 0
        for i in range(m):
            for j in range(n):
                if v[i][j] == 1:
                    tmp_cnt += 1
                    board[i][j] = 1
        answer += tmp_cnt
        # 탈출
        if tmp_cnt == 0:
            break

        # 아래로 붙이기.. 
        for i in range(m-2, -1, -1):
            for j in range(n):
                k = i
                while 0 <= k+1 < m and board[k+1][j] == 1:
                    k += 1
                if k != i:
                    board[k][j] = board[i][j]
                    board[i][j] = 1
        
#         def move(x,y):
#             cnt = 0
#             for i in range(x+1, m):
#                 if 0<=i<m and board[i][y] == 1:
#                     cnt+=1
#                 else:break
#             if cnt==0:
#                 return
#             else:
#                 char = board[x][y] 
#                 board[x][y]= 1
#                 board[x+cnt][y] = char
#                 v[x][y] = 1
#                 return

#         for i in range(m):
#             for j in range(n):
#                 move(i,j)
    return answer