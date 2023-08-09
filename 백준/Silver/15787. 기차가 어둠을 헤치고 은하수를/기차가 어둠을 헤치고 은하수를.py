import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [[0 for _ in range(21)] for _ in range(N+1)]
for i in range(M):
    order = list(map(int, input().split()))
    if order[0] == 1:
        arr[order[1]][order[2]] = 1
    elif order[0] == 2:
        arr[order[1]][order[2]] = 0
    elif order[0] == 3:
        arr[order[1]].insert(1,0)
        arr[order[1]].pop()
    elif order[0] == 4:
        arr[order[1]].pop(1)
        arr[order[1]].append(0)

set_arr = set()
del arr[0]
for i in arr:
    set_arr.add(tuple(i))
print(len(set_arr))

