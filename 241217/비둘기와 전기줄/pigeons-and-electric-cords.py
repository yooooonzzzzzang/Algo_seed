n = int(input())
arr = [-1] * 11
ans = 0
for _ in range(n):
    x,y = map(int,input().split())
    if arr[x] == -1:
        arr[x] = y
    else:
        if arr[x] != y:
            ans += 1
            arr[x] = y
print(ans)