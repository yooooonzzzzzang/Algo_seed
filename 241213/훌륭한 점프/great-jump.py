n,k = map(int,input().split())
arr = list(map(int,input().split()))


ans = 100
def solution(max_val):
    tmp = []
    for i, v in enumerate(arr):
        if v <= max_val:
            tmp.append(i)
    for i in range(1, len(tmp)):
        if tmp[i] - tmp[i-1] > k:
            return False
    return True

for i in range(max(arr[0], arr[n - 1]),101):
    if solution(i):
        ans = min(ans, i)
print(ans)