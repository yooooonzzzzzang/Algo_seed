n = int(input())
ans_1 = 0
ans_2 = 0
arr = [list(map(int, input().split())) for _ in range(n)]

def con_cur(x,y,n):
    global ans_1
    global ans_2
    chk = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if chk != arr[i][j]:
                con_cur(x,y, n//2)
                con_cur(x,y+n//2, n//2)
                con_cur(x+n//2,y, n//2)
                con_cur(x+n//2,y+n//2, n//2)
                return # 종료
    if chk == 0:
        ans_1 +=1
    else:
        ans_2 +=1
con_cur(0,0,n)
print(ans_1)
print(ans_2)