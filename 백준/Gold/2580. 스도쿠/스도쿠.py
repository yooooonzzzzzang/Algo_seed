'''
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
'''


arr = [list(map(int, input().split())) for _ in range(9)]

def checkRow(x,i):
    for idx in range(9):
        if arr[x][idx] == i:
            return False
    return True

def checkCol(y,i):
    for idx in range(9):
        if arr[idx][y] == i:
            return False
    return True
# 012 345 678

def checkRec(x,y,n):
    #lineX = x // 3 * 3
    #lineY = y //3 * 3
    #for nx in range(lineX, lineX+3):
    #    for ny in range(lineY, lineY+3):
    #        if arr[nx][ny] == i:
    #            return False
    #return True
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[x + i][y + j] == n:
                return False
    return True
def check(n):
    if n == len(blank):
        for i in arr:
            print(*i)
        exit()
    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]
        if checkRow(x,i) and checkCol(y,i) and checkRec(x,y,i):
            arr[x][y] = i
            check(n+1)
            arr[x][y] = 0

blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append([i,j])
check(0)