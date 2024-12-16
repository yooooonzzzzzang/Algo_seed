import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_v = sys.maxsize
max_v = -sys.maxsize

for x,y in arr:
    min_v = min(min_v, y)
    max_v = max(max_v, x)


if max_v <= min_v:
    print("Yes")
else:
    print("No")