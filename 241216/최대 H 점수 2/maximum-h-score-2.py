n, l = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0

# h점수
for h in range(1,101):
    flag = True
    cnt = 0
    l_cnt = l
    for j in range(n):
        if arr[j] < h:
            if arr[j] + 1 >= h and l_cnt > 0:
                cnt += 1
                l_cnt -= 1
        else:
            cnt +=1
    if cnt < h:
        flag = False

    if flag and l_cnt >= 0:
        ans = max(ans, h)
print(ans)