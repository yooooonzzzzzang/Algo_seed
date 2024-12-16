n,m = map(int,input().split())
arr = list(map(int,input().split()))

MAX_V = 10000 
ans = MAX_V
# i 최댓값
for i in range(1,MAX_V+1):
    tmp = 0
    section = 1
    flag = True
    for j in range(n):
        if arr[j] > i:
            flag = False
            break
        if tmp + arr[j] > i:
            tmp = 0
            section += 1
        tmp += arr[j]
    if flag and section == m:
        ans = min(ans,i)
print(ans)
