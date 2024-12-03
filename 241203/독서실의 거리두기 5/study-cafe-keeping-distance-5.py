n = int(input())
arr = list(map(int,input()))
# 0 ~ n +1 까지 직접 넣어보고 최대 거리를 계산 
prev = 0
ans = []
for i in range(n+1):
    arr.insert(i,1)
    tmp = []
    for j in range(n+1):
        if arr[j] == 1:
            tmp.append(j)
    max_a = 21
    for k in range(1,len(tmp)):
        max_a = min(tmp[k] - tmp[k-1], max_a)
    ans.append(max_a)


    del arr[i]
print(max(ans))