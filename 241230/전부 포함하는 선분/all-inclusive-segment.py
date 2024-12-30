import sys
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = sys.maxsize

for i in range(n):
    max_v = 0
    min_v = sys.maxsize
    for j in range(n):
        if i == j:
            continue
        max_v = max(arr[j][1], max_v)
        min_v = min(arr[j][0], min_v) 
    ans = min(max_v-min_v, ans)
print(ans)