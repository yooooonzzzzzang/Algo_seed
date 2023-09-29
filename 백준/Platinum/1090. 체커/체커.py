n = int(input())
x = []
y = []
ans = [-1] * n

for _ in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

for i in x:
    for j in y:
        distance = []
        for k in range(n):
            distance.append(abs(x[k]-i)+abs(y[k]-j))
        distance.sort()

        tmp = 0
        for l in range(len(distance)):
            d = distance[l]
            tmp += d
            if ans[l] == -1:
                ans[l] = tmp
            else:
                ans[l] = min(tmp, ans[l])
print(*ans)