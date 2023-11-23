n = int(input())
arr = list(map(int, input().split()))[::-1]
ans = [-1] * n
stack = []
# Ai의 오큰수는 오른쪽에 있으면서
# Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.

for i in range(n):
    now = arr[i]
    # 큐에 현재보다 왼쪽에 있는 애들 들어있음
    while stack:
        if stack[-1] <= now:
            stack.pop()
        else:
            # 1부터 시교
            ans[i] = stack[-1]
            break
    stack.append(arr[i])
print(*reversed(ans))
