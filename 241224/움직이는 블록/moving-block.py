n = int(input())
arr = [int(input()) for _ in range(n)]
goal = sum(arr) // n
# 평균 블럭보다 큰 블럭과 차이만큼 옮긴다.
ans = 0
for i in arr:
    if i > goal:
        ans += goal - i
print(ans)
