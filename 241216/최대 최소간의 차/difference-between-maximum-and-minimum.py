n,k = map(int,input().split())
arr = list(map(int,input().split()))
# 최소를 정하고 
# 최대는 i + k 
ans = 100000000
for min_v in range(1,10001):
    max_v = min_v+k
    cost = 0
    for j in arr:
        if j > max_v:
            cost += j - max_v
        elif j < min_v:
            cost += min_v - j
    ans = min(ans, cost)
print(ans)