n,k = map(int,input().split())
arr = [
    int(input())
    for _ in range(n)
]
ans = 0

def solution(l,m):
    cnt = 0
    for num in arr:
        if l <= num and num <= m:
            cnt += 1
    return cnt


# 뽑을 개수
for i in range(1,1001):
    ans = max(ans, solution(i,i+k))
print(ans)