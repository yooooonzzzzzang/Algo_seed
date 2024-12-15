n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
check = [0] * n
cnt = [0] * (n+1)


for i in range(n):
    for j in range(i+1, n):
        if j-i <= k and arr[i] == arr[j]:
            if check[j] == 0:
                check[j] = 1
                if check[i] == 0:
                    check[i] = 1
                    cnt[arr[i]] += 1
                cnt[arr[j]] += 1
max_ans = 0
max_idx = 0
for i in range(n+1):
    if cnt[i] >= max_ans:
        max_ans = cnt[i]
        max_idx = i
print(max_idx)