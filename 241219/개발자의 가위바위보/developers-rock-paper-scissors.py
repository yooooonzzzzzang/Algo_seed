n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt1 = 0
ans = 0 
# 1: 가위  2: 바위  3: 보
for i in range(n):
    if arr[i][0] == 1 and arr[i][1] ==3:
        cnt1 += 1
    elif arr[i][0] == 2 and arr[i][1] == 1:
        cnt1 += 1
    elif arr[i][0] == 3 and arr[i][1] ==2:
        cnt1 += 1
ans = max(ans, cnt1)
# 1: 가위  2: 보   3: 바위
cnt1 = 0
for i in range(n):
    if arr[i][0] == 1 and arr[i][1] ==2:
        cnt1 += 1
    elif arr[i][0] == 2 and arr[i][1] == 3:
        cnt1 += 1
    elif arr[i][0] == 3 and arr[i][1] ==1:
        cnt1 += 1
ans = max(ans, cnt1)
# 1: 바위  2: 가위  3: 보
cnt1 = 0
for i in range(n):
    if arr[i][0] == 1 and arr[i][1] ==2:
        cnt1 += 1
    elif arr[i][0] == 2 and arr[i][1] == 3:
        cnt1 += 1
    elif arr[i][0] == 3 and arr[i][1] ==1:
        cnt1 += 1
ans = max(ans, cnt1)
# 1: 바위  2: 보   3: 가위
cnt1 = 0
for i in range(n):
    if arr[i][0] == 1 and arr[i][1] ==3:
        cnt1 += 1
    elif arr[i][0] == 2 and arr[i][1] == 1:
        cnt1 += 1
    elif arr[i][0] == 3 and arr[i][1] ==2:
        cnt1 += 1
ans = max(ans, cnt1)

# 1: 보   2: 가위 3: 바위
cnt1 = 0
for i in range(n):
    if arr[i][0] == 1 and arr[i][1] ==3:
        cnt1 += 1
    elif arr[i][0] == 2 and arr[i][1] == 1:
        cnt1 += 1
    elif arr[i][0] == 3 and arr[i][1] ==2:
        cnt1 += 1
ans = max(ans, cnt1)
# 1: 보   2: 바위 3: 가위
cnt1 = 0
for i in range(n):
    if arr[i][0] == 1 and arr[i][1] ==2:
        cnt1 += 1
    elif arr[i][0] == 2 and arr[i][1] == 3:
        cnt1 += 1
    elif arr[i][0] == 3 and arr[i][1] ==1:
        cnt1 += 1
ans = max(ans, cnt1)
print(ans)