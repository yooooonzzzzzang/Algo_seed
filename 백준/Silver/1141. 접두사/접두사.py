n = int(input())
list = []
for _ in range(n):
    list.append(input())
list.sort()
ans = 0

for i in range(n):
    flag = True
    for j in range(i+1, n):
        if list[j].startswith(list[i]):
            flag = False
            break
    if flag:
        ans += 1

print(ans)